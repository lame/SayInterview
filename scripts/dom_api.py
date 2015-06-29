from lxml import etree, html

#  MUST USE PYTHON 2.x, libxml in python3 breaks iteration and tostring methods
def change_to_block_quote(page):
    in_file = page
    parser = etree.HTMLParser()
    tree = etree.parse(in_file, parser)

    for node in tree.xpath('//div[@contenteditable]//p'):
        node.tag='blockquote'

    return etree.tostring(tree, pretty_print=False, encoding="utf-8")
