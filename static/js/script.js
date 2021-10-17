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
      success: () => {
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
  $error.text('');

  var $resultsModal = $('body').find('.large-term-view');
  $resultsModal.find('.modal-content').empty()

  var $resultsHeader = $('<h1 class="title"></h1>')
  var $resultsContent = $('<p></p>')
  var $learnMore = $('<a></a>');

  $(".large-term-view").click(function(e) {
  
    $(".view-close").click(function(e) {
      $resultsModal.removeClass('is-active');
    });
  
    $(".view-background").click(function(e) {
      $resultsModal.removeClass('is-active');
    });
  });


  $.ajax({
    url: `/search/${$term.val()}`,
    type: "GET",
    dataType: "json",
    success: (resp) => {
        $resultsModal.addClass('is-active');

        $resultsHeader.text(resp[1]);
        $resultsContent.text(resp[0]);

        if (resp[0].includes(' ')) {
          const learnMoreString = resp[0].replace(' ', '+')
          $learnMore.attr("href", `https://www.google.com/search?q=${learnMoreString}`)
        } else {
          $learnMore.attr("href", `https://www.google.com/search?q=${resp[0]}`)
        }
        $learnMore.text('Learn more')
        $learnMore.attr('target','_blank');

        $resultsModal.find('.modal-content').append($resultsHeader);
        $resultsModal.find('.modal-content').append($resultsContent);
        $resultsModal.find('.modal-content').append($learnMore);
    },
    error: (resp) => {
        $error.text(resp.responseJSON.error)
        $termDiv.text('')
    }
  });
});

$("form[name=create-term-form").submit(function(e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/create",
    type: "POST",
    data: data,
    dataType: "json",
    success: (resp) => {
        $('body').find('.create').toggleClass('is-active');
    },
    error: (resp) => {
        $error.text(resp.responseJSON.error)
    }
  });
});

$("#create-term-modal").click(function(e) {
  $('body').find('.create').addClass('is-active');

  $(".modal-close").click(function(e) {
    $('body').find('.create').removeClass('is-active');
  });

  $(".modal-background").click(function(e) {
    $('body').find('.create').removeClass('is-active');
  });
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

$('.view-term-large').click((e) => {
  const id = e.currentTarget.id;
  const content = id.split(',');


  $('body').find('.modal-content').empty();

  const modal = $('body').find('.large-term-view');
  modal.addClass('is-active');

  $(".modal-close").click(function(e) {
    modal.removeClass('is-active');
  });

  $(".modal-background").click(function(e) {
    modal.removeClass('is-active');
  });

  var $resultsHeader = $(`<h1 class="title">${content[0]}</h1>`)
  var $resultsContent = $(`<p>${content[1]}</p>`)
  var $learnMore = $('<a></a>');

  if (content[1].includes(' ')) {
    const learnMoreString = content[1].replace(' ', '+')
    $learnMore.attr("href", `https://www.google.com/search?q=${learnMoreString}`)
  } else {
    $learnMore.attr("href", `https://www.google.com/search?q=${content[1]}`)
  }
  $learnMore.text('Learn more')
  $learnMore.attr('target','_blank');

  $('body').find('.modal-content').append($resultsHeader);
  $('body').find('.modal-content').append($resultsContent);
  $('body').find('.modal-content').append($learnMore);
});

$('.navbar-burger').click(() => {
  $('body').find('.navbar-burger').toggleClass('is-active');
  $('body').find('.navbar-menu').toggleClass('is-active');
})
