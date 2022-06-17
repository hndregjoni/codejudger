<template>
  <v-layout wrap fill-height>
    <v-flex>
      <v-tabs color="deep-purple accent-4" centered>
        <v-tab>Problem Statement</v-tab>
        <v-tab>Previous Submission</v-tab>
        <v-tab>Solutions</v-tab>

        <v-tab-item v-for="n in 3" :key="n">
          <v-container fluid>
            <v-row :key="i">
              <markdown-it-vue
                class="md-body"
                :content="'# Hello :) $x^2$'"
                :options="options"
              />
            </v-row>
          </v-container>
        </v-tab-item>
      </v-tabs>
    </v-flex>
    <v-flex>
      <v-container>
        <v-row class="primary" justify="space-between" align-center>
          <v-col cols="7 ">
            <v-select
              style="max-width: 200px"
              outlined
              dense
              :items="languages"
              placeholder="Languages"
              hide-details="true"
              background-color="white"
            ></v-select>
          </v-col>
          <v-col cols="auto"></v-col>
          <v-col cols="1">
            <v-btn class="ma-1" color="green" dense flat> Run </v-btn>
          </v-col>
          <v-col cols="2">
            <v-btn class="ma-1" color="blue black--text" dense flat>
              Submit
            </v-btn>
          </v-col>
        </v-row>
       
          <v-row >
            <codemirror 
              :style="{ position: 'fixed', height: '100%', width:'49.5%' }"
              ref="myCm"
              :matchBrackets="true"
              :autoCloseBrackets="true"
              :value="code"
              :options="cmOptions"
              @ready="onCmReady"
              @focus="onCmFocus"
              @input="onCmCodeChange"
          /></v-row>
      
      </v-container>
    </v-flex>
  </v-layout>
</template>

<style>
.vue-codemirror {
  display: flex;
  flex-direction: column;
 
}

.CodeMirror {
  flex-grow: 1;
}
</style>

<script>
// theme css
import "codemirror/theme/dracula.css";
// more codemirror resources
import "codemirror/addon/edit/matchbrackets.js";
import "codemirror/addon/wrap/hardwrap.js";

import "codemirror/addon/edit/closebrackets.js";
import "codemirror/mode/sql/sql.js";
import "codemirror/mode/python/python.js";
import "codemirror/mode/go/go.js";
import "codemirror/mode/haskell/haskell.js";
import "codemirror/mode/clojure/clojure.js";
import "codemirror/src/display/scrolling.js";

import "codemirror/addon/scroll/simplescrollbars.js";
// import 'codemirror/some-resource...'
export default {
  data() {
    return {
      languages: ["Python", "Java", "Go", "Clojure"],
      code: "const a = 10  ",
      cmOptions: {
        forceBreak: true,
        lineWrapping: true,
        matchBrackets: true,
        autoCloseBrackets: true,
        column: 30,
        // codemirror options
        tabSize: 4,
        mode: { name: "python" },
        theme: "dracula",
        lineNumbers: true,
        line: true,
      },
    };
  },
  methods: {
    onCmReady(cm) {
      console.log("the editor is readied!", cm);
    },
    onCmFocus(cm) {
      console.log("the editor is focus!", cm);
    },
    onCmCodeChange(newCode) {
      console.log("this is new code", newCode);
      this.code = newCode;
    },
  },
  computed: {
    codemirror() {
      return this.$refs.myCm.codemirror;
    },
  },
  mounted() {
    console.log("this is current codemirror object", this.codemirror);
    // you can use this.codemirror to do something...
  },
};
</script>