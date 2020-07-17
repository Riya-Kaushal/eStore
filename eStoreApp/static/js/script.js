

$(document).ready(function() {

    tab = $('.tabs h3 a');

      tab.on('click', function(event) {
        event.preventDefault();
        tab.removeClass('active');
        $(this).addClass('active');

        tab_content = $(this).attr('href');
        $('div[id$="tab-content"]').removeClass('active');
        $(tab_content).addClass('active');
      });

    console.log('Home screen');

      $('.sideMenuToggler').on('click', function() {
        $('.wrapper').toggleClass('active');
      });

      var adjustSidebar = function() {
        $('.sidebar').slimScroll({
          height: document.documentElement.clientHeight - $('.navbar').outerHeight()
        });
      };

      adjustSidebar();
      $(window).resize(function() {
        adjustSidebar();
      });
  });



// function register(id) {

//     name = $('input[name="update-name-'+id+'"]').val();
//     description = $('input[name="update-description-'+id+'"]').val();
//     csrfmiddlewaretoken = $('input[name="csrf"]').val();
//     // type = $('input[name="update-type-'+id+'"]').val();
//     processor = $('input[name="update-processor-'+id+'"]').val();
//     ram = $('input[name="update-ram-'+id+'"]').val();
//     screen_size = $('input[name="update-screen_size-'+id+'"]').val();
//     color = $('input[name="update-color-'+id+'"]').val();
//     hd_capacity = $('input[name="update-hd_capacity-'+id+'"]').val();


//     var radios = document.getElementsByName('update-type-'+id);
//     var selectedRadio = null;
//     console.log(radios);
//     for (var i = 0; i < radios.length; i++) {
//         if (radios[i].checked == true) {
//             selectedRadio = radios[i]; 
//             break;
//         }
//     }

//     var type = encodeURI(selectedRadio.value);


//     $.ajax({
//         type: 'POST',
//         url: '/update-product/',
//         data: {
//             'product-id' : id,
//             'name' : name,
//             'description' : description,
//             'csrfmiddlewaretoken': csrfmiddlewaretoken,
//             'product_type' : type,
//             'processor' : processor,
//             'ram' : ram,
//             'screen_size' : screen_size,
//             'color' : color,
//             'hd_capacity' : hd_capacity,
//         },
//         success: function(data) {
//             alert("This product has been updated.");
//             setTimeout(function() {
//                 location.reload();
//             }, 1500);
//         },
//         error: function(data, err) {
//             console.log(name + "\n " + description + "\n " + type + " \n" + processor+" \n"+ram+" \n"+ screen_size+ "\n" + color + "\n" +hd_capacity);
//             alert('Something missing! Please refill the form');
//         }
//     });
// };



function add_product() {

    name = $('input[name="name"]').val();
    description = $('input[name="description"]').val();
    csrfmiddlewaretoken = $('input[name="csrf"]').val();
    // type = $('input[name="update-type-'+id+'"]').val();
    processor = $('input[name="processor"]').val();
    ram = $('input[name="ram"]').val();
    screen_size = $('input[name="screen_size"]').val();
    color = $('input[name="color"]').val();
    hd_capacity = $('input[name="hd_capacity"]').val();


    var radios = document.getElementsByName('type');
    var selectedRadio = null;
    console.log(radios);
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked == true) {
            selectedRadio = radios[i]; 
            break;
        }
    }

    var type = encodeURI(selectedRadio.value);


    $.ajax({
        type: 'POST',
        url: '/add-product/',
        data: {
            'name' : name,
            'description' : description,
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'product_type' : type,
            'processor' : processor,
            'ram' : ram,
            'screen_size' : screen_size,
            'color' : color,
            'hd_capacity' : hd_capacity,
        },
        success: function(data) {
            alert("Hurray! Added a new Product.");
            setTimeout(function() {
                location.reload();
            }, 1500);
        },
        error: function(data, err) {
            console.log(name + "\n " + description + "\n " + type + " \n" + processor+" \n"+ram+" \n"+ screen_size+ "\n" + color + "\n" +hd_capacity);
            alert('Something missing! Please refill the form');
        }
    });
};





function update_product(id) {

    name = $('input[name="update-name-'+id+'"]').val();
    description = $('input[name="update-description-'+id+'"]').val();
    csrfmiddlewaretoken = $('input[name="csrf"]').val();
    // type = $('input[name="update-type-'+id+'"]').val();
    processor = $('input[name="update-processor-'+id+'"]').val();
    ram = $('input[name="update-ram-'+id+'"]').val();
    screen_size = $('input[name="update-screen_size-'+id+'"]').val();
    color = $('input[name="update-color-'+id+'"]').val();
    hd_capacity = $('input[name="update-hd_capacity-'+id+'"]').val();


    var radios = document.getElementsByName('update-type-'+id);
    var selectedRadio = null;
    console.log(radios);
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked == true) {
            selectedRadio = radios[i]; 
            break;
        }
    }

    var type = encodeURI(selectedRadio.value);


    $.ajax({
        type: 'POST',
        url: '/update-product/',
        data: {
            'product-id' : id,
            'name' : name,
            'description' : description,
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
            'product_type' : type,
            'processor' : processor,
            'ram' : ram,
            'screen_size' : screen_size,
            'color' : color,
            'hd_capacity' : hd_capacity,
        },
        success: function(data) {
            alert("This product has been updated.");
            setTimeout(function() {
                location.reload();
            }, 1500);
        },
        error: function(data, err) {
            console.log(name + "\n " + description + "\n " + type + " \n" + processor+" \n"+ram+" \n"+ screen_size+ "\n" + color + "\n" +hd_capacity);
            alert('Something missing! Please refill the form');
        }
    });
};



function delete_product(id) {
    csrfmiddlewaretoken = $('input[name="csrf"]').val();

    $.ajax({
        type: 'POST',
        url: '/delete-product/',
        data: {
            'product-id' : id,
            'csrfmiddlewaretoken': csrfmiddlewaretoken,
        },
        success: function(data) {
            alert("This product has been deleted.");
            setTimeout(function() {
                location.reload();
            }, 1500);
        },
        error: function(data, err) {
            alert('Something missing! Please refill the form');
        }
    });
};



function addProductModal(){
    // alert('Great! Meals recorded successfully');
    $('#add-product').modal('show');
  }

function updateProductModal(id){
    $('#update-product-'.concat(id)).modal('show');
  }

function deleteProductModal(id){
    $('#delete-product-'.concat(id)).modal('show');
    // $('#update-product'.concat(id)).modal('show');
  }



