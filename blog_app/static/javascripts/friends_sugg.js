$(".btn-sm").click(
    function()
    {
        

        var user_id = $(this).data('user-id');
        console.log(user_id)
        $.ajax
        (
           {
            url: "follow/",
            method : 'POST',
            data : 
            {
                user_id_for_following: user_id
            },
            success: function(response) {
                // Handle successful response from server
                
                swal({
                    title: "You are now following " + response['user_name_of_following'] + "!",
                    text: "you can now see his/her posts in your feed!",
                    icon: "success",
                    buttons: ["Cancel", "OK"],
                    dangerMode: true,
                })
                .then((confirmed) => {
                    if (confirmed) {
                    // If the user clicked "OK", reload the page
                    location.reload();
                    }
                });
                
              
              },
              error: function(xhr, status, error) {
                    // Handle error response from server
                    console.log(xhr.responseText);
                    // Show a styled SweetAlert dialog
                    // Show a confirmation dialog using SweetAlert
                    swal({
                        title: "Warning?",
                        text: "you are not able to following your self!",
                        icon: "warning",
                        buttons: ["Cancel", "OK"],
                        dangerMode: true,
                    })
                    .then((confirmed) => {
                        if (confirmed) {
                        // If the user clicked "OK", reload the page
                        location.reload();
                        }
                    });
  
              }
           }
           

        )
        
    }
);


