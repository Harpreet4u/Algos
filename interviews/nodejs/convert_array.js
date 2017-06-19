// Don't know the exact logic, other logic could be just picking powers of 2 numbers and adding their squares.

var convert = (a,b) => {
  let arr = [];
  let res = [];
  for (var i = 0;i<(a.length-1);i+=2) {
    arr.push(a[i+1]-a[i]);
  }
  arr.forEach(function(number, index){
    if (index>0){
      var val = number+arr[index-1];
      res[index] = val*val + '';
    } else {
      res[index] = number*number + '';
    }
  });
  console.log(res);
}

convert([2, 4, 6, 8, 9, 15], ['4', '16', '64'])
