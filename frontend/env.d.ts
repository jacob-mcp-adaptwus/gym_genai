interface ImportMetaEnv {
    readonly VITE_API_URL: string;
    readonly VITE_COGNITO_AUTHORITY: string;
    readonly VITE_COGNITO_CLIENT_ID: string;
    readonly VITE_COGNITO_REGION: string;
    readonly VITE_COGNITO_DOMAIN: string;
  }
  


  interface ImportMetaEnv {
    readonly VITE_APP_TITLE: string
    readonly BASE_URL: string
    readonly VITE_API_URL: string
  }
  
  interface ImportMeta {
    readonly env: ImportMetaEnv
    readonly url: string
  }
  
  declare module '*.png' {
    const src: string
    export default src
  }
  
  declare module '*.jpg' {
    const src: string
    export default src
  }
  
  declare module '*.jpeg' {
    const src: string
    export default src
  }
  
  declare module '*.svg' {
    const src: string
    export default src
  }
  
  declare module '*.gif' {
    const src: string
    export default src
  }