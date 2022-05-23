import { Plugin } from '@nuxt/types';

const plugin: Plugin = ({ $axios, $config, store }, inject) => {
    $axios.setBaseURL($config.apiBase);
}
export default plugin;