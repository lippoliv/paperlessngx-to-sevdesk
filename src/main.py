import glob
import json
import os
import string
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Final

import requests
from requests import Response


@dataclass()
class Config:
    paperlessngx_url: str = None
    paperlessngx_token: str = None
    paperlessngx_filter_tag_id: str = None
    paperlessngx_filter_document_type_id: str = None
    sevdesk_token: str = None
    run_interval: int = None

    def is_valid(self):
        if not self.paperlessngx_url:
            return False

        if not self.paperlessngx_token:
            return False

        if not self.sevdesk_token:
            return False

        return True


sevdesk_url: Final[string] = "https://my.sevdesk.de/api/v1"
last_downloaded_document_id: int = 0
config: Config = Config(
    paperlessngx_url=os.getenv('PAPERLESSNGX_URL') or "",
    paperlessngx_token=os.getenv('PAPERLESSNGX_TOKEN') or "",
    paperlessngx_filter_tag_id=os.getenv('PAPERLESSNGX_FILTER_TAG_ID') or 0,
    paperlessngx_filter_document_type_id=os.getenv('PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID') or 0,
    sevdesk_token=os.getenv('SEVDESK_TOKEN') or 0,
    run_interval=int(os.getenv('RUN_INTERVAL')) or 300,
)


def paperlessngx_get(path: string) -> Response:
    return requests.get(
        config.paperlessngx_url + path,
        allow_redirects=False,
        headers={
            "Authorization": "Token " + config.paperlessngx_token
        }
    )


def paperlessngx_lookup_new_documents():
    global last_downloaded_document_id

    # lookup documents
    lookup_url = ("/api/documents/?query=added:%5B-1%20week%20to%20now%5D" +
                  "&sort=created" +
                  "&reverse=1")

    if config.paperlessngx_filter_tag_id:
        lookup_url += "&tags__id__all=" + config.paperlessngx_filter_tag_id

    if config.paperlessngx_filter_document_type_id:
        lookup_url += "&document_type__id__in=" + config.paperlessngx_filter_document_type_id

    response = paperlessngx_get(
        lookup_url
    )
    data = json.loads(response.content)
    new_document_ids = sorted(data['all'])
    if last_downloaded_document_id == 0:
        if len(new_document_ids):
            last_downloaded_document_id = new_document_ids[len(new_document_ids) - 1]

        return

    # download found documents
    for current_document_id in new_document_ids:
        if current_document_id <= last_downloaded_document_id:
            continue

        print("Downloading " + str(current_document_id))
        response = paperlessngx_get(
            "/api/documents/" + str(current_document_id) + "/download/"
        )
        file = Path("workdir/" + str(current_document_id) + ".pdf")
        file.write_bytes(response.content)

        last_downloaded_document_id = current_document_id


def sevdesk_upload_file(local_file_path: string) -> bool:
    read_file = open(local_file_path, 'rb')
    response = requests.post(
        sevdesk_url + "/Voucher/Factory/createVoucherFromFile",
        headers={
            "Authorization": config.sevdesk_token,
            "Accept": "application/json",
        },
        data={'creditDebit': 'C'},
        files={"voucher": (os.path.basename(local_file_path), read_file)}
    )

    return response.status_code == 201


def sevdesk_upload_workdir():
    for file in glob.glob("workdir/*.pdf"):
        print("Uploading " + file)
        if sevdesk_upload_file(file):
            os.unlink(file)
        else:
            print("- failed")


def main():
    if not config.is_valid():
        print("Config invalid")
        print("You need to at leaset specify the following environment variables:")
        print("- PAPERLESSNGX_URL")
        print("- PAPERLESSNGX_TOKEN")
        print("- SEVDESK_TOKEN")
        exit(1)

    while True:
        paperlessngx_lookup_new_documents()
        sevdesk_upload_workdir()

        time.sleep(config.run_interval)


if __name__ == '__main__':
    main()
