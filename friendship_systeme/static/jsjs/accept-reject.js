var usrs = $(".btn-primary");
//localStorage.setItem("users", usrs);
//console.log(localStorage.getItem("users"));

for (i of $(".btn-primary"))
{
    usrs.push($(i).data('user-id'));
    i.removeAttribute('data-user-id');

};
console.log(usrs);




//$(".btn").removeAttribute("data-user-id");

$(".btn-primary").click(
    function() {

      var usr = $(this).data('user-id');
      console.log(usr);

      $.ajax
        (
           {
            url: "accept",
            method : 'POST',
            data : 
            {
                user_to_accept:usr
            },

            success:function (respons)
            {
                console.log(respons);
                window.location.reload();
            },
           
           }
        )




  } 
  );




$(".btn-danger").click(
function()
{
    var uuid = $(this).data("user-id")

    console.log(uuid)
    $.ajax
    (
        {
            url: "reject",
            method: "POST",
            data:
            {
                usr_uuid: uuid,
            },
            success:function (respons)
            {
            
                console.log(respons);
                window.location.reload();
            
            },

        }
    );
}




);
