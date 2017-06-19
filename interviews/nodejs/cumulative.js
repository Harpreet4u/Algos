// finding cumulative ttl of given requests.

let requests = [
  {requestId: 'poiax',  startedAt: 1489744808, ttl: 8},
  {requestId: 'kdfhd',  startedAt: 1489744803, ttl: 3},
  {requestId: 'uqwyet', startedAt: 1489744806, ttl: 12}, 
  {requestId: 'qewaz',  startedAt: 1489744810, ttl: 1}
]

var get_min = (a, b) => {
  return a < b ? a : b;
}

var get_max = (a, b) => {
  return a > b ? a : b;
}

var cttl = (requests) => {
  var min = 0, max = 0;
  requests.forEach((req, index) => {
    if (index > 0) {
      min = get_min(req.startedAt, min);
    } else {
      min = req.startedAt;
    }
    max = get_max(req.startedAt + req.ttl, max)
  });

  return max - min;
}


console.log(cttl(requests));

