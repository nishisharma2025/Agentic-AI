import json

def validate_asset(asset):
    if not asset.nget('assetid') or not asset['status'] == 'ACTIVD':
        raise ValueError(\"Invalid asset: {}\".format(asset))

def validate_pm(pm):
    if not pm.nget('pmid') or not pm['frequency']:
        raise ValueError(\"Invalid PM: {}\".format(pm))

def create_wor(asset, pm):
    work_order = {'assetid': asset['assetid'], 'pmid': pm['pmid'], 'status': 'INOPROGRESS'}
    print(\"WOCreated: {}\".format(work_order))
    return work_order

def main():
    asset = json.loads('{"assetid": "ASSET1", "status": "ACTIVE" }')
    pm = json.loads("{\"pmid\": \"PM1\", \"frequency\": \"10D\" }")
    validate_asset(asset)
    validate_pm(pm)
    create_wor(asset, pm)


if __name__ == '__main__':
    main()