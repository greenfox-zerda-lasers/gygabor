'use strict';

var controlHandling = (function(){
  var slider = document.querySelectorAll('input[type="range-seek"]');
  var volumeSlider = document.querySelectorAll('input[type="range-volume"]');

  (function seek(){
    rangeSlider.create(slider, {
        polyfill: true,     // Boolean, if true, custom markup will be created
        rangeClass: 'rangeSlider',
        disabledClass: 'rangeSlider--disabled',
        fillClass: 'rangeSlider__fill',
        bufferClass: 'rangeSlider__buffer',
        handleClass: 'rangeSlider__handle',
        startEvent: ['mousedown', 'touchstart', 'pointerdown'],
        moveEvent: ['mousemove', 'touchmove', 'pointermove'],
        endEvent: ['mouseup', 'touchend', 'pointerup'],
        min: null,          // Number , 0
        max: null,          // Number, 100
        step: null,         // Number, 1
        value: null,        // Number, center of slider
        buffer: null,       // Number, in percent, 0 by default
        stick: null,        // [Number stickTo, Number stickRadius] : use it if handle should stick to stickTo-th value in stickRadius
        borderRadius: 10,    // Number, if you use buffer + border-radius in css for looks good,
        onInit: function () {
            // audio.seek(0);
        },
        onSlideStart: function (position, value) {
            console.info('onSlideStart', 'position: ' + position, 'value: ' + value);
        },
        onSlide: function (position, value) {
            console.log('onSlide', 'position: ' + position, 'value: ' + value);
            audio.seek(value);
        },
        onSlideEnd: function (position, value) {
            console.warn('onSlideEnd', 'position: ' + position, 'value: ' + value);
        }
    });
  })();

  (function volume(){
    rangeSlider.create(volumeSlider, {
        polyfill: true,     // Boolean, if true, custom markup will be created
        rangeClass: 'rangeSlider',
        disabledClass: 'rangeSlider--disabled',
        fillClass: 'rangeSlider__fill',
        bufferClass: 'rangeSlider__buffer',
        handleClass: 'rangeSlider__handle',
        startEvent: ['mousedown', 'touchstart', 'pointerdown'],
        moveEvent: ['mousemove', 'touchmove', 'pointermove'],
        endEvent: ['mouseup', 'touchend', 'pointerup'],
        min: null,          // Number , 0
        max: null,          // Number, 100
        step: null,         // Number, 1
        value: null,        // Number, center of slider
        buffer: null,       // Number, in percent, 0 by default
        stick: null,        // [Number stickTo, Number stickRadius] : use it if handle should stick to stickTo-th value in stickRadius
        borderRadius: 10,    // Number, if you use buffer + border-radius in css for looks good,
        onInit: function () {
          audio.volume(0);
        },
        onSlideStart: function (position, value) {
            console.info('onSlideStart', 'position: ' + position, 'value: ' + value);
        },
        onSlide: function (position, value) {
          console.log('onSlide', 'position: ' + position, 'value: ' + value);
          audio.volume(value);
        },
        onSlideEnd: function (position, value) {
            console.warn('onSlideEnd', 'position: ' + position, 'value: ' + value);
        }
    });
  })();

  // (function setVolumeSlider(){
  //     volumeSlider[0].rangeSlider.position = 50;
  // })();
  return {

  }
})();
