var a="Aakash"
var b=10
var c=true
var d=null

var g

typeof(g)

var a=10

if(a==="10"){
    console.log("Hello")
}else if(a==10){
    //
}

else{
 console.log("False")   
}
let i
for( i=0;i<10;i++)
{
    console.log(i)
}
console.log(i)

let l=2
switch(l){
    case 1:{
        console.log(1)
        break;
    }
    case 2:{
        console.log(2)
    }
    case 3:{
        console.log(3)
        break;
    }
    case 4:{
        console.log(4)
    }
    default:{
        console.log("Default")
    }
}

let z=10
// while(z<10){
//     console.log(z)
//     z++
// }

do{
    console.log(z++)
    
}while(z<10)

var fruits=["Apple","Banana","Cherry"]

//forEach loop

fruits.forEach((a, index)=>{
    console.log(`${index +1 }: ${a}`);
})

var demo="Demo20"

console.log(`this is ${demo}`)