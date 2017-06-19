var fs = require('fs');

fs.readFile('file.txt', function(err, data) {
    if(err) throw err;
    var array = data.toString().split("\n");
    var triangles = [];
    var rectangles = [];
    var squares = [];
    var everythingElse = [];

    for(i in array) {
        var arr = array[i].split(',');
        if (arr.length == 1 && arr[0] == '') continue;
        var len_arr = arr.map((val)=>parseInt(val));
        
        if (len_arr.length == 3) {
          let cnt = 0;
          len_arr.map((val, idx, arr)=>{
            if ((arr[idx%3]+arr[idx%3])>arr[idx%3]){
              cnt ++;
            }
          
          });
          if (cnt === 3) {
            triangles.push(len_arr);
          } else {
            everythingElse.push(len_arr);
          }
        } else if (len_arr.length == 4) {
          if (len_arr.every((val, idx, arr)=>val==arr[0])) {
            squares.push(len_arr);
          } else {
            let sortedArr = len_arr.slice();
            sortedArr.sort();
            if (sortedArr[0]===sortedArr[1] && 
                sortedArr[2]===sortedArr[3]) {

              rectangles.push(len_arr);
            } else {
              everythingElse.push(len_arr);
            }
          }
        } else {
          everythingElse.push(len_arr);
        }
      
    }

    console.log("Triangles: ", triangles);
    console.log("Rectangles: ", rectangles);
    console.log("Squares: ", squares);
    console.log("Everything Else: ", everythingElse);
});

