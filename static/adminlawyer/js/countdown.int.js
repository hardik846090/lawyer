$(document).ready(function(){$(function(){$(".comming-watch .countdown").countdown({date:"January 17, 2020 20:39:00",render:function(s){$(this.el).html('<div><div class="card card-body p-3"><span class="countdown-num">'+(parseInt(365*this.leadingZeros(s.years,2))+parseInt(this.leadingZeros(s.days,2)))+'</span><span class="text-uppercase">days</span></div><div class="card card-body p-3"><span class="countdown-num">'+this.leadingZeros(s.hours,2)+'</span><span class="text-uppercase">hours</span></div></div><div class="lj-countdown-ms "><div class="card card-body p-3"><span class="countdown-num">'+this.leadingZeros(s.min,2)+'</span><span class="text-uppercase">minutes</span></div><div class="card card-body p-3"><span class="countdown-num">'+this.leadingZeros(s.sec,2)+'</span><span class="text-uppercase">seconds</span></div></div>')}})})});