$("form[name=register-form").submit(function(e) {
    e.preventDefault();
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/register",
      type: "POST",
      data: data,
      dataType: "json",
      success: (resp) => {
          window.location.href = '/dashboard/'
      },
      error: (resp) => {
          $error.text(resp.responseJSON.error)
      }
    });
  });

$("form[name=login-form").submit(function(e) {
    e.preventDefault();
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/user/login",
      type: "POST",
      data: data,
      dataType: "json",
      success: (resp) => {
          window.location.href = '/dashboard/'
      },
      error: (resp) => {
          $error.text(resp.responseJSON.error)
      }
    });
});

$("form[name=search-form").submit(function(e) {
  e.preventDefault();
  var $form = $(this);
  var $term = $form.find('#term')
  var $error = $form.find(".error");
  var $termDiv = $('body').find('.term-def');


  $.ajax({
    url: `/search/${$term.val()}`,
    type: "GET",
    dataType: "json",
    success: (resp) => {
        $termDiv.text(resp)
    },
    error: (resp) => {
        $error.text(resp.responseJSON.error)
        $termDiv.text('')
    }
  });
});

$("form[name=create-term-form").submit(function(e) {
  e.preventDefault();
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/create",
    type: "POST",
    data: data,
    dataType: "json",
    success: (resp) => {
        console.log(resp)
    },
    error: (resp) => {
        $error.text(resp.responseJSON.error)
    }
  });
});

$("#create-term-modal").click(function(e) {
  $('body').find('.modal').addClass('is-active');

  $(".modal-close").click(function(e) {
    $('body').find('.modal').removeClass('is-active');
  });

  $(".modal-background").click(function(e) {
    $('body').find('.modal').removeClass('is-active');
  });

  // $(".create-button").click(function(e) {
  //   $('body').find('.modal').removeClass('is-active');
  // });
});

$(".edit-term").click(function(e) {
  const termToEdit = e.currentTarget.parentElement.id;
  const modal = $('body').find('.edit-modal');
  modal.addClass('is-active')

  modal.find('.edit-title').text(termToEdit);

  e.preventDefault();
  var $form = $(this);
  var $error = $form.find(".error");

  $(".modal-close").click(function(e) {
    modal.removeClass('is-active');
  });

  $(".modal-background").click(function(e) {
    modal.removeClass('is-active');
  });

  $("form[name=edit-term-form").submit(function(e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: `/edit/${termToEdit}`,
      type: "POST",
      data: data,
      dataType: "json",
      success: () => {
        modal.removeClass('is-active');
      },
      error: (resp) => {
        $error.text(resp.responseJSON.error)
      }
    });
  });
});

$(".delete-term").click(function(e) {
  const termToDelete = e.currentTarget.parentElement.id;
  const modal = $('body').find('.delete-modal');
  modal.addClass('is-active')

  modal.find('.delete-target').text(termToDelete)

  var $form = $(this);
  var $error = $form.find(".error");

  $(".modal-close").click(function(e) {
    modal.removeClass('is-active');
  });

  $(".modal-background").click(function(e) {
    modal.removeClass('is-active');
  });

  $(".cancel-delete").click(function(e) {
    modal.removeClass('is-active');
  });

  $(".final-delete").click(function(e) {
    $.ajax({
      url: `/delete/${termToDelete}`,
      type: "POST",
      dataType: "json",
      success: () => {
        modal.removeClass('is-active');
      },
      error: (resp) => {
        $error.text(resp.responseJSON.error)
      }
    });
    location.reload()
  });
});