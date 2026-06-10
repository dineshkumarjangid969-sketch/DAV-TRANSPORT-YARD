
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'docling-service'))
from app import DoclingParser

def test_set_rule_2():
    parser = DoclingParser()
    # Mock text based on SET rule 2.png
    text = """
Harvey Norman Stores (NZ) Pty Ltd
Harvey Norman Bedding Mt Wellington
20-54 Mt Wellington Highway
Mt Wellington N.Z.
Phone: 09 570 3440

Reprinted : 09/06/26 13:03:29
Order : 82304
TAX INVOICE
INVOICE REPRINT 22/3833887

*** G.S.T. EXEMPT ***

HARVEY NORMAN COMMERICAL BEDDING PORIRUA
PORIRUA WN 5022

*** F2F STOCK SALES ***
F2F Sale Details
PO Number : 82304
Requested By : WILLIAM REEVES

Product Qty Price Total
* L3WMMB03 6 $139.59 $837.54
ALPHINE 3DRW BEDSIDE
* L3WMMB012 6 $378.42 $2,270.52
ALPHINE 6DRW TALLBOY

Invoice Notes
"""
    result = parser.extract_order_data(text, [])
    print(f"Order: {result['order_number']}")
    print(f"Invoice: {result['invoice_number']}")
    print(f"Type: {result['type']}")
    print(f"BT From: {result['bt_from']}")
    print(f"BT To: {result['bt_to']}")
    print(f"Items: {result['line_items']}")

    assert result['order_number'] == '82304'
    assert result['invoice_number'] == '3833887'
    assert result['type'] == 'branch_transfer'
    assert result['bt_from'] == 'Mt Wellington'
    assert result['bt_to'] == 'Porirua'
    assert len(result['line_items']) == 2
    assert result['line_items'][0]['sku'] == 'L3WMMB03'
    assert result['line_items'][0]['quantity'] == 6
    assert 'ALPHINE 3DRW BEDSIDE' in result['line_items'][0]['description']

def test_goods_movement_1():
    parser = DoclingParser()
    # Mock text based on Goods movement 1.png
    text = """
Harvey Norman Stores (NZ) Pty Ltd
H.N. AV/IT Commercial Wairau Park
10 Croftfield Lane
Wairau Park Auckland 0627

Assistant : 9077/237 ALANA W
Order : 215596
TAX INVOICE
INVOICE 29/653122

*** G.S.T. EXEMPT ***

HN PALMERSTON NTH ELECTRICAL
361/371 MAIN ST WEST AL
PALMERSTON NORTH PM 5301

*** F2F STOCK SALES ***
F2F Sale Details
PO Number : 215596

Product Description Qty Price Total
* CI904CTB1 F&P CLASSIC INDUCTION 90CM COOKTOP 1 $2,164.00 $2,164.00
"""
    result = parser.extract_order_data(text, [])
    print(f"Order: {result['order_number']}")
    print(f"Invoice: {result['invoice_number']}")
    print(f"Type: {result['type']}")
    print(f"BT From: {result['bt_from']}")
    print(f"BT To: {result['bt_to']}")
    print(f"Items: {result['line_items']}")

    assert result['order_number'] == '215596'
    assert result['invoice_number'] == '653122'
    assert result['type'] == 'branch_transfer'
    assert result['bt_from'] == 'Wairau Park'
    assert result['bt_to'] == 'Palmerston North'
    assert len(result['line_items']) == 1
    assert result['line_items'][0]['sku'] == 'CI904CTB1'
    assert result['line_items'][0]['quantity'] == 1

if __name__ == "__main__":
    try:
        test_set_rule_2()
        print("test_set_rule_2 passed")
        test_goods_movement_1()
        print("test_goods_movement_1 passed")
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
