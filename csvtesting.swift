public var uscities = "/docs/csv/uscities.csv"
public var crimedata = "/docs/csv/crime_data_w_population_and_crime_rate.csv"
public var citieszip = "/docs/csv/report.csv"

//input city name string, returns zip code string
func getCityGivenZip (zipinp: String) -> String {
  do {
       let csvData = try String(contentsOfFile: citieszip)
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

//input zip code string, returns city string
func getZipGivenCity (cityInp: String) -> String {
  do {
       let csvData = try String(contentsOfFile: citieszip)
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

/*

func findC (countyname, statename : String) -> String {
  do {

       let csvData = try String(contentsOfFile: uscities)
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
      print(error)
  }
}

*/


//function to recall crime states. find specific one by calling self.county_name, self.crime_rate_per_100000, self.MURDER, etc.
func returncrimestats(countyname: String) -> (county_name: String, crime_rate_per_100000: Float, index: String, EDITION: Int, Part: Int, IDNO: Int, CPOPARST: Int, AG_ARRST: Int, AG_OFF: Int, COVIND: Int, INDEX: Int, MODINDX: Int, MURDER: Int, RAPE: Int, ROBBERY: Int, AGASSLT: Int, BURGLRY: Int, LARCENY: Int, MVTHEFT: Int, ARSON: Int, population: Int, FIPS_ST: Int, FIPS_CITY: Int) { //enter countyname
    let csvData = try String(contentsOfFile: citieszip)
    let csv = csvData.csvRows()
    let arrayofcrimes = []
    for row in csv {
         let array = row.components(separatedBy: ",")
         if (String(array[0]).lowercased() == countyname.lowercased()){
             Swift.print(String(array))
             arrayofcrimes = array
             break
         }
         else{
           Swift.print("county not found, please check spelling")
         }

         Swift.print(arrayofcrimes)
         return(arrayofcrimes[0],arrayofcrimes[1],arrayofcrimes[2],arrayofcrimes[3],arrayofcrimes[4],arrayofcrimes[5],arrayofcrimes[6],arrayofcrimes[7],arrayofcrimes[8],arrayofcrimes[9],arrayofcrimes[10],arrayofcrimes[11],arrayofcrimes[12],arrayofcrimes[13],arrayofcrimes[14],arrayofcrimes[15],arrayofcrimes[16],arrayofcrimes[17],arrayofcrimes[18],arrayofcrimes[19],arrayofcrimes[20],arrayofcrimes[21],arrayofcrimes[22],arrayofcrimes[23])

      //   categories are
      //   county_name,crime_rate_per_100000,index,EDITION,PART,IDNO,CPOPARST,CPOPCRIM,AG_ARRST,AG_OFF,COVIND,INDEX,MODINDX,MURDER,RAPE,ROBBERY,AGASSLT,BURGLRY,LARCENY,MVTHEFT,ARSON,population,FIPS_ST,FIPS_CTY

}

/*
func mean() -> () {


}
*/
