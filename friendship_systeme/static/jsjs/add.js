$( ".btn-primary" ).click(
    function() {

      var usr = $(this).data('user-id');
      console.log(usr);

      $.ajax
        (
           {
            url: "add_friend",
            method : 'POST',
            data : 
            {
                user_to_add:usr
            },

            success:function (respons)
            {
              console.log(respons)
            },
           
           }
        )




  } 
  );


