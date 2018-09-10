function add_fav(pro_id,type,e)
{
	var getURL=location.href
	event.stopImmediatePropagation();
	console.log(getURL)
	if(!is_login)
	{
		$('#loginModal').modal();
	}
	else{
		if(getURL.indexOf('detail')>0){
		}
		else{
			$(e).toggleClass('fav-sel');
		}
	}
	if(pro_id > 0)
	{
		$.ajax({
			url:fav_url,
			type:"post",
			dataType:'json',
			async:true,
			data:{
				pro_id:pro_id,
				type:type
			},
			success:function(result) {
				var data = result.datas;
				
				if(result.login == 1)
				{
					//alert(data.error);
					//location.href = login_url;
					$('#loginModal').modal();
				}
				else if(data == 1)
				{
					$('.swiper-container .fav[pro_id="'+pro_id+'"]').toggleClass('fav-sel');
				}
				else
				{
					alert(data.error);
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown) {
				
			}
		});
	}
}

/*
 * èŽ·å–å½“æ—¥æœŸ
 * fmtï¼š æ”¯æŒæ ¼å¼y-m-d h:i:s
 */
function get_date(fmt)
{
	var nowDate = new Date();
	var year = nowDate.getFullYear();
	var month = nowDate.getMonth() + 1;
	var day = nowDate.getDate();
	var hour = nowDate.getHours();
	var minute = nowDate.getMinutes();
	var second = nowDate.getSeconds();
	
	month = month >= 10?month:'0'+month;
	day = day >= 10?day:'0'+day;
	hour = hour >= 10?hour:'0'+hour;
	minute = minute >= 10?minute:'0'+minute;
	second = second >= 10?second:'0'+second;
	
	if(fmt == undefined || fmt == '' || fmt == null)
	{
		fmt = 'y-m-d';
	}
	
	fmt = fmt.replace(/y/i, year);
	fmt = fmt.replace(/m/i, month);
	fmt = fmt.replace(/d/i, day);
	fmt = fmt.replace(/h/i, hour);
	fmt = fmt.replace(/i/i, minute);
	fmt = fmt.replace(/s/i, second);
	
	return fmt;
}

function strtotime(datetime)
{
    var tmp_datetime = datetime.replace(/:/g,'-');
    tmp_datetime = tmp_datetime.replace(/ /g,'-');
    var arr = tmp_datetime.split("-");
    var now = new Date(Date.UTC(arr[0],arr[1]-1,arr[2],arr[3]-8,arr[4],arr[5]));
    return parseInt(now.getTime()/1000);
}

// ç§’è½¬æ¢ä¸º xx:xx:xx
function second_to_hour(timeDiff)
{
	var days          = timeDiff / 60 / 60 / 24;
    var daysRound     = Math.floor(days);
    var hours         = timeDiff / 60 / 60 - (24 * daysRound);
    var hoursRound    = Math.floor(hours);
    var minutes       = timeDiff /60 - (24 * 60 * daysRound) - (60 * hoursRound);
    var minutesRound  = Math.floor(minutes);
    var seconds       = timeDiff  - (24 * 60 * 60 * daysRound) - (60 * 60 * hoursRound) - (60 * minutesRound);
    var secondsRound  = Math.floor(seconds);
	
    return '<span>'+ daysRound +'</span> å¤© '+'<span>'+ hoursRound +'</span>'+' : <span>'+ minutesRound +'</span> : <span>'+ secondsRound +'</span>';
}

function count_down(selector)
{
	setInterval(function(){
        $(selector).each(function(){
            var time_now = get_date('y-m-d h:i:s');
            var time_to = $(this).attr('data-time');
            var time_tip = $(this).attr('data-tip'); // å®ŒæˆåŽæç¤º
            time_now = strtotime(time_now);
            time_to = strtotime(time_to);
            var timeDiff = time_to - time_now;
            if(timeDiff <= 0) {
                $(this).html(time_tip);
                return false;
            }

            var str = second_to_hour(timeDiff);
            $(this).html(str);
            //console.log(str);
        });
    }, 1000);
}
$(function() {
	$('.trip-item').click(function(){
		var url = $(this).attr('url');
		if(url)
		{
			location.href = url;
		}
	});
});


/*å›¾ç‰‡å¤§å°æµ‹è¯•*/