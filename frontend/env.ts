interface EnvVariables {
    apiBase: string | undefined,
    appName: string | undefined
}

export const extractFromEnv = (env:any) :EnvVariables => {
    const _env = process.env.VUE_APP_ENV;

    let _apiBase = '';

    if (_env === 'prod') {
        let portProd = process.env.VUE_APP_PORT_PROD;
        if (portProd)
            _apiBase = `https://${process.env.VUE_APP_DOMAIN_PROD}:${portProd}`;
        else
            _apiBase = `https://${process.env.VUE_APP_DOMAIN_PROD}`;
    } else if (_env === 'stag') {
        let portStag = process.env.VUE_APP_PORT_STAG;
        if (portStag)
            _apiBase = `https://${process.env.VUE_APP_DOMAIN_STAG}:${portStag}`;
        else
            _apiBase = `https://${process.env.VUE_APP_DOMAIN_STAG}`;
    } else  if (_env === 'dev') {
        let portDev = process.env.VUE_APP_PORT_DEV;
        if (portDev)
            _apiBase = `https://${process.env.VUE_APP_DOMAIN_DEV}:${portDev}`;
        else
            _apiBase = `https://${process.env.VUE_APP_DOMAIN_DEV}`;
    }

    return {
        'apiBase': _apiBase + '/api/v1',
        'appName': process.env.VUE_APP_NAME
    }
}