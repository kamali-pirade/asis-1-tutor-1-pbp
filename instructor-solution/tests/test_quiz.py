import re
from html.parser import HTMLParser
from pathlib import Path

from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from bookquiz.views import landing_page


ROOT = Path(settings.BASE_DIR)
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Markup(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.nodes = []
        self.stack = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = {"tag": tag, "attrs": dict(attrs), "children": [], "text": ""}
        if self.stack:
            self.stack[-1]["children"].append(node)
        self.nodes.append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1]["tag"] == tag:
            self.stack.pop()

    def handle_data(self, data):
        if self.stack:
            self.stack[-1]["text"] += data


def descendants(node):
    for child in node["children"]:
        yield child
        yield from descendants(child)


def inner_text(node):
    return node["text"] + "".join(inner_text(child) for child in node["children"])


def page():
    return Markup((ROOT / "templates" / "index.html").read_text())


def css():
    source = (ROOT / "static" / "css" / "style.css").read_text()
    return re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)


def rule(source, selector):
    match = re.search(r"(?<![\w-])" + re.escape(selector) + r"\s*\{([^{}]*)\}", source)
    return match.group(1) if match else ""


class GitHygieneTests(SimpleTestCase):
    def test_todo_1_ignores_credentials_and_database(self):
        entries = set((ROOT / ".gitignore").read_text().splitlines())
        self.assertTrue({".env*", "db.sqlite3"} <= entries)

    def test_todo_1_ignores_environments_and_caches(self):
        entries = set((ROOT / ".gitignore").read_text().splitlines())
        self.assertTrue({"env/", "venv/", "__pycache__/", "*.pyc"} <= entries)


class PageRoutingTests(SimpleTestCase):
    def test_todo_2_root_has_named_route_to_view(self):
        self.assertEqual(reverse("landing_page"), "/")
        self.assertIs(resolve("/").func, landing_page)

    def test_todo_2_root_renders_static_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class NavigationTests(SimpleTestCase):
    def test_todo_3_navigation_links_to_both_sections(self):
        markup = page()
        headers = [node for node in markup.nodes if node["tag"] == "header"]
        self.assertEqual(len(headers), 1)
        navs = [node for node in descendants(headers[0]) if node["tag"] == "nav"]
        self.assertEqual(len(navs), 1)
        links = {node["attrs"].get("href") for node in descendants(navs[0]) if node["tag"] == "a"}
        self.assertTrue({"#intro", "#pilihan"} <= links)


class IntroTests(SimpleTestCase):
    def test_todo_4_semantic_intro_has_useful_text(self):
        markup = page()
        sections = [node for node in markup.nodes if node["tag"] == "section" and node["attrs"].get("id") == "intro"]
        self.assertEqual(len(sections), 1)
        headings = [node for node in descendants(sections[0]) if node["tag"] == "h1"]
        paragraphs = [node for node in descendants(sections[0]) if node["tag"] == "p"]
        self.assertEqual(len(headings), 1)
        self.assertGreater(len(inner_text(headings[0]).strip()), 5)
        self.assertTrue(any(len(inner_text(item).strip()) >= 40 for item in paragraphs))

    def test_todo_4_intro_uses_supplied_image_with_alt_text(self):
        markup = page()
        sections = [node for node in markup.nodes if node["tag"] == "section" and node["attrs"].get("id") == "intro"]
        self.assertEqual(len(sections), 1)
        images = [node for node in descendants(sections[0]) if node["tag"] == "img"]
        self.assertTrue(any("bookshelf.svg" in image["attrs"].get("src", "") and len(image["attrs"].get("alt", "").strip()) >= 8 for image in images))
        self.assertIsNotNone(finders.find("img/bookshelf.svg"))


class IntroStyleTests(SimpleTestCase):
    def test_todo_5_intro_has_desktop_layout(self):
        source = css()
        hero = rule(source, ".hero")
        self.assertRegex(hero, r"display\s*:\s*(grid|flex)\s*;")
        self.assertRegex(hero, r"(gap|grid-template-columns|justify-content)\s*:")


class PicksTests(SimpleTestCase):
    def test_todo_6_new_section_has_three_semantic_items(self):
        markup = page()
        sections = [node for node in markup.nodes if node["tag"] == "section" and node["attrs"].get("id") == "pilihan"]
        self.assertEqual(len(sections), 1)
        articles = [node for node in descendants(sections[0]) if node["tag"] == "article"]
        self.assertGreaterEqual(len(articles), 3)

    def test_todo_6_each_item_has_title_and_description(self):
        markup = page()
        sections = [node for node in markup.nodes if node["tag"] == "section" and node["attrs"].get("id") == "pilihan"]
        self.assertEqual(len(sections), 1)
        articles = [node for node in descendants(sections[0]) if node["tag"] == "article"]
        self.assertGreaterEqual(len(articles), 3)
        titles = []
        for article in articles:
            headings = [node for node in descendants(article) if node["tag"] in {"h2", "h3"}]
            paragraphs = [node for node in descendants(article) if node["tag"] == "p"]
            self.assertTrue(headings)
            self.assertTrue(any(len(inner_text(item).strip()) >= 20 for item in paragraphs))
            titles.append(inner_text(headings[0]).strip())
        self.assertEqual(len(titles), len(set(titles)))


class PicksStyleTests(SimpleTestCase):
    def test_todo_7_new_section_uses_flex_or_grid(self):
        self.assertRegex(rule(css(), ".pick-grid"), r"display\s*:\s*(grid|flex)\s*;")

    def test_todo_7_cards_have_dedicated_styling(self):
        card = rule(css(), ".pick-card")
        self.assertRegex(card, r"(padding|background|border)\s*:")
        self.assertGreaterEqual(card.count(":"), 2)


class ResponsiveTests(SimpleTestCase):
    def test_todo_8_mobile_query_adapts_both_layouts(self):
        source = css()
        match = re.search(r"@media\s*\(\s*max-width\s*:\s*(\d+)px\s*\)\s*\{([\s\S]*)\}\s*$", source)
        self.assertIsNotNone(match)
        self.assertLessEqual(int(match.group(1)), 768)
        media = match.group(2)
        self.assertRegex(rule(media, ".hero"), r"(grid-template-columns|flex-direction)\s*:")
        self.assertRegex(rule(media, ".pick-grid"), r"(grid-template-columns|flex-direction)\s*:")
