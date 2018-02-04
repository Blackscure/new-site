 

document.getElementById("chngbkcolor").onclick = function(event)
{
    document.getElementById("sampDiv").style.backgroundColor=" #EFDECD";

}
// document.getElementById("chgImg").onclick = function(event){
//     document.getElementById("sampDiv").style.backgroundImage ="url('repeatBkgrnd.png')";
// }
document.getElementById("chgBorderstyle").onclick = function(event){
        document.getElementById("sampDiv").style.borderstyle="solid";
}

document.getElementById("chngBorderstyle").onclick = function(event){
        document.getElementById(sampDiv).style.bordercolor ="blue";
}

var fruit = 'orange';

switch(fruit){
    case"banana":
    alert('i hate banana');
    break;
    case"apple":
    alert('i love apple');
    break;
    case"oranges":
    alert('i love all other fruits');

}