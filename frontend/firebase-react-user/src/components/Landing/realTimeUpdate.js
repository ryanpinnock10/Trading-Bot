function getData() {
    return Math.random();
}  
Plotly.plot('chart',[{
    y:[getData()],
    type:'line'
}]);

var cnt = 0;
setInterval(function(){
    Plotly.extendTraces('chart',{ y:[[getData()]]}, [0]);
    cnt++;
    if(cnt > 500) {
        Plotly.relayout('chart',{
            xaxis: {
                range: [cnt-500,cnt]
            }
        });
    }
},15);