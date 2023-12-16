var insert = function(intervals, newInterval) {
    let merged = [];

    for (let i=0; i<intervals.length; i++){
        if (newInterval[1]<intervals[i][0]){
            merged.push(newInterval);
            return merged.concat(intervals.slice(i));
        }
        else if (newInterval[0]>intervals[i][1]){
            merged.push(intervals[i]);
        }
        else {newInterval = [Math.min(intervals[i][0],newInterval[0]),Math.max(intervals[i][1],newInterval[1])]}
    }
    merged.push(newInterval) ; 
    return merged ; 
};