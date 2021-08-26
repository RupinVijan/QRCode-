const head=document.getElementById("heading");
const foot=document.getElementById("foot");
const btn=document.getElementById("btn");
const inp=document.getElementById("inp");

const text="QR CODE GENERATOR";
const text1="MADE BY.- RUPIN VIJAN"
        let index=1;
        let index1=1;
        function writee(){
            head.innerText=text.slice(0,index);
            foot.innerText=text1.slice(0,index1);
            index++;
            index1++;
            if (index>text.length){
                index=1;
            }
            if (index1>text1.length){
                index1=1;
            }
        }
        setInterval(() => {
            writee();
        }, 300);
