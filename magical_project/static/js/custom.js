$('#search-key').keyup(function(){$('#search-key').removeClass('error')})

$( "#search-form" ).submit(function( event ) {
  	event.preventDefault();
  	
	var search_key =  $('#search-key').val();
 	var job_opening = $("#job_opening").is(":checked") ? 1: 0;
 	var search_employees_inf = $("#employee_info").is(":checked") ? 1 : 0;
 	var search_company_inf = $("#company_info").is(":checked") ? 1 : 0;
 	var filter_applied = (job_opening == 0 && search_employees_inf == 0 && search_company_inf == 0) ? 'NO' :'YES';
 
 	if ($('#search-key').val() == ""){
 		$('#search-key').addClass('error');
 	}else{
 		$('#search-key').removeClass('error')
	 	$.ajax({
                url: '/get-serach-result/',
                type: 'GET',
                data: {'search_job_opeings':job_opening,'search_employees_inf':search_employees_inf,'search_company_inf':search_company_inf,'search_key':search_key, 'filter_applied':filter_applied },
                
                success: function(data) {
                	if (data['success'] && data['data'].length > 0 ){

                		var head = '<ol>'
                		var tail = '</ol>'
                		var body = ''
                		$('.list-search').html('');

                		for (i=0;i<data['data'].length > 0;i++){
                            if (data['data'][i]['table'] === 'job'){
                			body += '<li><p><em><b>Job Opening Role: </b> <a>'+data['data'][i]['name'] +'</a></em></p></li>'
                			body += '<p><b>Search Result Type  : </b>'+data['data'][i]['type_of_data'] +'</p>\n</li>'
                			body += '<p><b>Description  : </b>'+data['data'][i]['description'] +'</p><hr>'
                                
                            }else if (data['data'][i]['table'] === 'employee'){
                            body += '<li><p><em><b>Employee Name: </b> <a>'+data['data'][i]['name'] +'</a></em></p></li>'
                            body += '<p><b>Search Result Type  : </b>'+data['data'][i]['type_of_data'] +'</p>\n</li>'
                            body += '<p><b>Employee Role  : </b>'+data['data'][i]['employee_role'] +'</p>\n</li>'
                            body += '<p><b>Description  : </b>'+data['data'][i]['description'] +'</p><hr>'
                                
                            }else if (data['data'][i]['table'] === 'company'){
                            body += '<li><p><em><b>Company Name: </b> <a>'+data['data'][i]['name'] +'</a></em></p></li>'
                            body += '<p><b>Search Result Type  : </b>'+data['data'][i]['type_of_data'] +'</p>\n</li>'
                            body += '<p><b>Company Description  : </b>'+data['data'][i]['description'] +'</p><hr>'
                                
                            }
                			
                		}

                		$('.list-search').append(head + body + tail);

                	}
                	else if ( data['data'].length == 0 ){
                		$( "div.warning" ).fadeIn( 1000 ).delay( 1500 ).fadeOut( 1000 );
	                		
                	}
                },
                error: function(xhr, status, error) {
                    alert("Something went wrong onserver side")
                }
            })
 	}
 
});






 