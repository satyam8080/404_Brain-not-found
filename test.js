/*use node to run this javascript code */


 "use strict";
        var myInit = {
            method : 'GET',
            headers :{
            'content-type':'appliaction/json'
            },
            mode :'cors',
            cache : 'default'
        }
        var request = new Request("./jason.json",myInit);
        var st = "";
        
        
        
        fetch(request)
            .then(function(resp){
            return resp.json();
        })
            .then(function(data){
          

            
            for(var i=0;i<data.data.length;i++)
                {
                    for(var j=2;j<7;j++){
                        st = st +data.data[i][j]+","
                    }
                    st = st.substring(0,st.length - 1);
                    st = st + "\n"
                    
                }
          /* console.log( st)*/
    
            
            var f = require('fs');
f.writeFile('dataset.csv', st , function (err) {
  if (err) throw err;
  console.log('Replaced!');
});
          
          
        })
        