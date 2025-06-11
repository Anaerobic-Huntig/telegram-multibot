"""Simple Google Sheets importer placeholder."""

from __future__ import annotations

from typing import Iterable

import gspread
from google.oauth2.service_account import Credentials


async def import_sheet(credentials_json: str, sheet_url: str) -> Iterable[dict]:
    creds = Credentials.from_service_account_file(credentials_json, scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"])
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url).sheet1
    rows = sheet.get_all_records()
    for row in rows:
        yield {
            "name": row.get("name"),
            "description": row.get("description"),
            "price": float(row.get("price", 0)),
            "image_url": row.get("image_url"),
        }
