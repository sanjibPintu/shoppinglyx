
$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
const url="http://127.0.0.1:8000/"


// for ajax part in + -
$('.plus-cart').click(
    function ()
    {
       var id=$(this).attr('pid').toString()
        var pluselm=this.parentNode.children[2]
       $.ajax({
           type: "GET",
           url: `${url}pluscart/`,
           data: {
               prod_id:id
           },
           
           success: function (response) {
            console.log(response)
            pluselm.innerText=response.quantity
            document.getElementById('totalprice').innerText=parseFloat(response.originalprice) 
            document.getElementById('youhavetopay').innerText= parseFloat(response.youhavetpay)
            document.getElementById('discount').innerText=response.discount
              
           }
       });
      
    }

)
// for ajax - cart
$('.minus-cart').click(
    function ()
    {
       var id=$(this).attr('pid').toString()
        var pluselm=this.parentNode.children[2]
       $.ajax({
           type: "GET",
           url: `${url}minuscart/`,
           data: {
               prod_id:id
           },
           
           success: function (response) {
            console.log(response)
            pluselm.innerText=response.quantity
            document.getElementById('totalprice').innerText=parseFloat(response.originalprice) 
            document.getElementById('youhavetopay').innerText= parseFloat(response.youhavetpay)
            document.getElementById('discount').innerText=response.discount
              
           }
       });
      
    }

)

// for remove -cart
$('.remove-cart').click(
    function ()
    {
    var id=$(this).attr('pid').toString()
    var elm=this
       $.ajax({
           type: "GET",
           url: `${url}removecart/`,
           data: {
               prod_id:id
           },
           
           success: function (response) {
            document.getElementById('totalprice').innerText=parseFloat(response.originalprice) 
            document.getElementById('youhavetopay').innerText= parseFloat(response.youhavetpay)
            document.getElementById('discount').innerText=response.discount
            elm.parentNode.parentNode.parentNode.parentNode.remove()
           }
       });
      
    }

)


// checking and chenging cart value
// setInterval(()=>
// {
//     $.ajax({
//         type: "GET",
//         url: `${url}checkcat`,
//         success: function (response) {
//             console.log(response)
//             document.getElementById('totalcart').innerText=response.totalcart
//         }
//     });
// },5000)
