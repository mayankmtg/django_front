var leftIcons = document.getElementsByClassName("iconbar");
var questionBlocks=document.getElementsByClassName("modal-content");

var i;
for (i=0;i<questionBlocks.length;i++){
	questionBlocks[i].classList.add("hide");
	leftIcons[i].onclick = function(arg){
		return function() {
			console.log(arg);
			var elements=document.getElementsByClassName("modal-content");
			var leftElements = document.getElementsByClassName("iconbar");
			for (var k = 0; k < elements.length; k++){
				if(k!=arg){
					elements[k].classList.add("hide");
					leftElements[k].classList.remove("active");
				}
				else{
					leftElements[k].classList.add("active");
					elements[k].classList.remove("hide");
				}
			}
		}
	}(i);
}

var done=document.getElementById("Done");
done.onclick=function(){
	document.getElementById("userdetail").classList.add("hide");
	document.getElementById("sub").classList.remove("hide");
	var elements=document.getElementsByClassName("modal-content");
	for (var k = 0; k < elements.length; k++){
		elements[k].classList.add("hide");
	}
	var done2=document.getElementById("sub");
	done2.style.display="block";
};

var start=document.getElementById("starttest");
start.onclick = function(){
	var left_icon_bar=document.getElementById("icon-bar");
	left_icon_bar.classList.remove("hide");
	var elements=document.getElementsByClassName("modal-content");
	var leftElements = document.getElementsByClassName("iconbar");
	elements[0].classList.remove("hide");
	leftElements[0].classList.add("active");
}

var auth=document.getElementById("Auth");
auth.onclick = function(){
	document.getElementById("userdetail").classList.remove("hide");
	document.getElementById("sub").classList.add("hide");
	var left_icon_bar=document.getElementById("icon-bar");
	left_icon_bar.classList.add("hide");
	var elements=document.getElementsByClassName("modal-content");
	var leftElements = document.getElementsByClassName("iconbar");
	elements[0].classList.add("hide");
	leftElements[0].classList.remove("active");
}




