
import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'docling-service'))
from app import DoclingParser

def test_user_reported_issues():
    parser = DoclingParser()

    # Issue 124099
    text1 = "268.50 268.50 0.00 268.50 THE INCREDI-BED DBL BASE Deliver Not Before: 07/06/26"
    result1 = {"line_items": []}
    parser._extract_line_items_from_text(text1, result1)
    print(f"124099 Items: {result1['line_items']}")
    assert len(result1['line_items']) == 1
    assert result1['line_items'][0]['description'] == "THE INCREDI-BED DBL BASE"

    # Issue 716194
    text2 = "$2,869.00 $2,869.00 WILLOW 3+2 LTH BLK Delivery Scheduled 11/06/26 Store To Door Delivery Service"
    result2 = {"line_items": []}
    parser._extract_line_items_from_text(text2, result2)
    print(f"716194 Items: {result2['line_items']}")
    assert len(result2['line_items']) == 1
    assert result2['line_items'][0]['description'] == "WILLOW 3+2 LTH BLK"

    # Issue 225661
    text3 = "BT from HN Pukekohe to HN Wairau Park - BT INV 5225661\nKW202632LTH  WILLOW 3+2 LTH BLK QTY 1"
    result3 = {"line_items": []}
    parser._extract_line_items_from_text(text3, result3)
    print(f"225661 Items: {result3['line_items']}")
    assert len(result3['line_items']) == 1
    assert result3['line_items'][0]['sku'] == "KW202632LTH"
    assert result3['line_items'][0]['quantity'] == 1

    # Issue 140375
    text4 = "DVH9-09W	1699.04 1699.04 254.86 1953.90	1"
    result4 = {"line_items": []}
    parser._extract_line_items_from_text(text4, result4)
    print(f"140375 Items: {result4['line_items']}")
    assert len(result4['line_items']) == 1
    assert result4['line_items'][0]['sku'] == "DVH9-09W"
    assert result4['line_items'][0]['quantity'] == 1

if __name__ == "__main__":
    try:
        test_user_reported_issues()
        print("All user reported issue tests passed!")
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()
