function CalculationExportToPDF() {
    var pdf = new jsPDF('p', 'pt', 'letter', true);;
    
    var resource = pdf.autoTableHtmlToJson($("#calculations-table").get(0));
    // pdf.autoTable(resource.columns, resource.data, {margin: {top: 80}});
  
    var header = function(data) {
        pdf.setFontSize(18);
        pdf.setTextColor(40);
        pdf.setFontStyle('normal');
        //doc.addImage(headerImgData, 'JPEG', data.settings.margin.left, 20, 50, 50);
        pdf.text("Country List", data.settings.margin.left, 50);
      };
    
      var options = {
        beforePageContent: header,
        margin: {
          top: 80
        },
    
        // startY: pdf.autoTableEndPosY() + 20
      };
    
      pdf.autoTable(resource.columns, resource.data, options);

    var blob = pdf.output("blob");
    window.open(URL.createObjectURL(blob));
    // pdf.save('test.pdf');
}
