import json
import os
import string
import time
from pathlib import Path

import requests
from requests import Response

last_downloaded_document_id = 0


def paperlessngx_get(path: string) -> Response:
    return requests.get(
        os.environ['PAPERLESSNGX_URL'] + path,
        allow_redirects=False,
        headers={
            "Authorization": "Token " + os.environ['PAPERLESSNGX_TOKEN']
        }
    )


def paperlessngx_lookup_new_documents():
    global last_downloaded_document_id

    # lookup documents
    response = paperlessngx_get(
        "/api/documents/?query=added:%5B-1%20week%20to%20now%5D" +
        "&tags__id__all=" + os.environ['PAPERLESSNGX_FILTER_TAG_ID'] + "" +
        "&document_type__id__in=" + os.environ['PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID'] + "" +
        "&sort=created" +
        "&reverse=1"
    )
    data = json.loads(response.content)
    new_document_ids = sorted(data['all'])
    if last_downloaded_document_id == 0:
        last_downloaded_document_id = new_document_ids[len(new_document_ids) - 1]
        return

    # download found documents
    for current_document_id in new_document_ids:
        if current_document_id <= last_downloaded_document_id:
            continue

        response = paperlessngx_get(
            "/api/documents/" + str(current_document_id) + "/download/"
        )
        file = Path("workdir/" + str(current_document_id) + ".pdf")
        file.write_bytes(response.content)

        last_downloaded_document_id = current_document_id


def main():
    while True:
        paperlessngx_lookup_new_documents()

        time.sleep(int(os.environ['RUN_INTERVAL']))


if __name__ == '__main__':
    main()
