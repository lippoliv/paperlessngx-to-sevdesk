# PaperlessNGX to sevDesk

Poll new files from PaperlessNGX and push them to sevDesk as new voucher.

## Configuration

The following environment variables are used for configuration

| Name                                 | Description                                                               |
|--------------------------------------|---------------------------------------------------------------------------|
| RUN_INTERVAL                         | **Optional:** How often to scan for new files (default: 300)              |
| PAPERLESSNGX_URL                     | The PaperlessNGX url (e.g. `https://paperle.ss`)                          |
| PAPERLESSNGX_TOKEN                   | The PaperlessNGX token to be used for fetching new files                  |
| PAPERLESSNGX_FILTER_TAG_ID           | **Optional:** The PaperlessNGX tag (ID) to filter documents for           |
| PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID | **Optional:** The PaperlessNGX document type (ID) to filter documents for |
| SEVDESK_TOKEN                        | The sevDesk token to be used for uploading files                          |

## Installation

You can easily run this as a docker compose project:

```yaml
version: "3"

services:
  worker:
    image: lippertsweb/paperlessngx-to-sevdesk:latest
    environment:
      # You PaperlessNGX url (e.g. "https://paperle.ss" or "http://192.168.0.1:8080")
      PAPERLESSNGX_URL: "..."

      # You can get your PaperlessNGX token by clicking your icon (top-right on the screen) and select "Profile"
      PAPERLESSNGX_TOKEN: "..."

      # Optional: The tag to filter for (can help to seperate private and busines documents)
      # PAPERLESSNGX_FILTER_TAG_ID: 7

      # Optional: The document type id to filter for (probably you just want invoices to be uploaded)
      # PAPERLESSNGX_FILTER_DOCUMENT_TYPE_ID: 1

      # You can get token from user management screen (https://my.sevdesk.de/admin/userManagement)
      SEVDESK_TOKEN: "..."

      # Optional: Run all five minutes (5 minutes * 60 seconds = 300 seconds)
      # RUN_INTERVAL: 300
```

# Thanks

Many thanks to the [PaperlessNGX](https://github.com/paperless-ngx/paperless-ngx) team for the hard work and the nice
and stable open source project :)