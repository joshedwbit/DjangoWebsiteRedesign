console.log('formmmm')

const allStars=document.querySelectorAll('.star');
let current_rating=document.querySelector('.current-rating');
// console.log(allStars);
allStars.forEach((star,i)=>{
    star.onclick=function(){
        // console.log(star);
        // console.log(i+1);
        let indexed_star_level=i+1;
        let current_star_level=5-i;
        current_rating.innerText=`${current_star_level} of 5`
        // console.log(current_star_level)
        allStars.forEach((star,j)=>{
            // console.log(j+1);
            if(indexed_star_level<=j+1)
            {
                star.innerHTML='&#9733';
            }else{
                star.innerHTML='&#9734'
            }
        })
    }
}
)

const selectedAll=document.querySelectorAll(".selected");

selectedAll.forEach(selected=>{
    const optionsContainer=selected.previousElementSibling;
// dont need all since only 1 selected tag etc
const optionsList=optionsContainer.querySelectorAll(".option")
// multiple options tags
selected.addEventListener("click",()=>{
    if(optionsContainer.classList.contains("active")){
        optionsContainer.classList.remove("active");
    }else{
        let currentActive=document.querySelector(".options-container.active");

        if (currentActive){
            currentActive.classList.remove("active");
        }
        optionsContainer.classList.add("active");
    }
    // optionsContainer.classList.toggle("active");
    // 'toggle' either adds or takes away the active class
});

optionsList.forEach(o=>{
    // o references any single element
    o.addEventListener("click",()=>{
        selected.innerHTML=o.querySelector("label").innerHTML;
        optionsContainer.classList.remove("active");
        // once clicked, will give selected the value of the label
    });
})
})



const selected=document.querySelector(".selected");
const optionsContainer=document.querySelector(".options-container")
// dont need all since only 1 selected tag etc
const optionsList=document.querySelectorAll(".option")
// multiple options tags
selected.addEventListener("click",()=>{
    optionsContainer.classList.toggle("active");
    // 'toggle' either adds or takes away the active class
});

optionsList.forEach(o=>{
    // o references any single element
    o.addEventListener("click",()=>{
        selected.innerHTML=o.querySelector("label").innerHTML;
        optionsContainer.classList.remove("active");
        // once clicked, will give selected the value of the label
    });
})
