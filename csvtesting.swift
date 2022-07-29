do {
     let csvData = try String(contentsOfFile: "file")
     let csv = csvData.csvRows()
     let str = ""
     for row in csv {
          let array = row.components(separatedBy: ",")
          print(array)
     }
} catch {
    print(error)
}
