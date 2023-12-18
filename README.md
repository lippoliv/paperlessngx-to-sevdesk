# PaperlessNGX to sevDesk

Simplify and streamline your document management with the [PaperlessNGX](https://docs.paperless-ngx.com/)
to [sevDesk](https://sevdesk.de/) application. This lightweight and efficient tool automates the transfer of files from
PaperlessNGX to sevDesk, seamlessly integrating your document workflow. This application ensures that your expense
documents are accurately recorded and available in sevDesk.

Configuring the application is straightforward using environment variables. The flexibility of the configuration
empowers you to customize the application according to your document categorization preferences.

Installation is a breeze with Docker Compose, and the provided example clearly guides you through the setup process. The
application's continuous loop ensures that it consistently monitors for new documents, providing a hands-free solution
to keep your sevDesk account up-to-date. Take control of your document management, save time, and ensure accuracy with
the PaperlessNGX to sevDesk application.

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