
// require lib
import Vue from 'vue'
import VueCodeMirror from 'vue-codemirror'
// import 'codemirror/mode/javascript/javascript.js'

// require styles
import 'codemirror/lib/codemirror.css'

// require more codemirror resource...

// you can set default global options and events when use
Vue.use(VueCodeMirror, 
  { 
  options: { theme: 'base16-dark' },
  events: ['scroll']
} )


