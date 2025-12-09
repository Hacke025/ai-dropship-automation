function doPost(e) {
  const sheet = SpreadsheetApp.openById("1MfO45nxRqwFCfONyb3FDoQOdm9gMRt2lEXy70eUAzDg");
  const sheetTab = sheet.getSheetByName("Orders");

  const data = JSON.parse(e.postData.contents);

  sheetTab.appendRow([
    new Date(),
    data.product,
    data.source,
    data.link
  ]);

  return ContentService.createTextOutput("OK");
}
