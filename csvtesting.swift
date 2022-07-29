/*do {
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
*/
func getCityGivenZip (zipinp: String) -> String {
  do {
       let csvData = try String(contentsOfFile: "file")
       let csv = csvData.csvRows()
       let str = ""
       for row in csv {
            let array = row.components(separatedBy: ",")
            if (String(array[0]) == zipinp){
                return(String(array[3]))
            }
            else{
            }
       }
  } catch {
      print(error)
  }
}

func getZipGivenCity (cityInp: String) -> String {
  do {
       let csvData = try String(contentsOfFile: "file")
       let csv = csvData.csvRows()
       let str = ""
       for row in csv {
            let array = row.components(separatedBy: ",")
            if (String(array[3]).lowercased() == cityInp.lowercased()){
                return(String(array[0]))
            }
            else{
            }
       }
  } catch {
      print(error)
  }
}



func findC (countyname, statename : String) -> String {
  do {

       let csvData = try String(contentsOfFile: "/docs/csv/uscities.csv")
       let csv = csvData.csvRows()
       let arr = []
       for row in csv {
            let array = row.components(separatedBy: ",")
            if (String(array[2]).lowercased() == statename.lowercased()){
                if (String(array[5]).lowercased() == county_name.lowercased()){
                    return True
                }
                else{

                }
            }
            else{
            }
       }
  } catch {
      print(error) */
  }
}
