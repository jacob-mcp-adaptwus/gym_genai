const AuthRoutes = {
  path: '/auth',
  component: () => import('@/layouts/blank/BlankLayout.vue'),
  meta: {
    requiresAuth: false
  },
  children: [
    {
      name: 'Landingpage',
      path: '/',
      component: () => import('@/views/pages/landingpage/LandingPage.vue')
    },
    {
      name: 'ContactUs',
      path: '/pages/contact-us',
      component: () => import('@/views/pages/landingpage/ContactUs.vue')
    },
    {
      name: 'PrivacyPolicy',
      path: '/pages/privacy-policy',
      component: () => import('@/views/pages/landingpage/PrivacyPolicy.vue')
    },
    {
      name: 'FAQs',
      path: '/pages/faq',
      component: () => import('@/views/pages/landingpage/FAQs.vue')
    },
    {
      name: 'Info',
      path: '/info',
      component: () => import('@/views/pages/landingpage/Info.vue')
    },
    {
      name: 'Login 2',
      path: '/auth/login2',
      component: () => import('@/views/authentication/auth2/LoginPage2.vue')
    },
    {
      name: 'Register 2',
      path: '/auth/register2',
      component: () => import('@/views/authentication/auth2/RegisterPage2.vue')
    },
    {
      name: 'Forgot Password 2',
      path: '/auth/forgot-pwd2',
      component: () => import('@/views/authentication/auth2/ForgotPwd2.vue')
    },
    {
      name: 'Check Mail 2',
      path: '/auth/check-mail2',
      component: () => import('@/views/authentication/auth2/CheckMail2.vue')
    },
    {
      name: 'Reset Password 2',
      path: '/auth/reset-pwd2',
      component: () => import('@/views/authentication/auth2/ResetPwd2.vue')
    },
    {
      name: 'Code Verification 2',
      path: '/auth/code-verify2',
      component: () => import('@/views/authentication/auth2/CodeVerification2.vue')
    },
    {
      name: 'Authentication 3',
      path: '/auth/login3',
      component: () => import('@/views/authentication/auth3/AuthenticationPage3.vue')
    },
    {
      name: 'Login',
      path: '/auth/login1',
      component: () => import('@/views/authentication/auth1/LoginPage1.vue')
    },
    {
      name: 'Register',
      path: '/auth/register1',
      component: () => import('@/views/authentication/auth1/RegisterPage1.vue')
    },
    {
      name: 'Forgot Password',
      path: '/auth/forgot-pwd1',
      component: () => import('@/views/authentication/auth1/ForgotPwd1.vue')
    },
    {
      name: 'Check Mail',
      path: '/auth/check-mail1',
      component: () => import('@/views/authentication/auth1/CheckMail1.vue')
    },
    {
      name: 'Reset Password',
      path: '/auth/reset-pwd1',
      component: () => import('@/views/authentication/auth1/ResetPwd1.vue')
    },
    {
      name: 'Code Verification',
      path: '/auth/code-verify1',
      component: () => import('@/views/authentication/auth1/CodeVerification1.vue')
    },
    {
      name: 'Coming Soon 1',
      path: '/pages/comingsoon1',
      component: () => import('@/views/pages/maintenance/comingsoon/ComingSoonPage1.vue')
    },
    {
      name: 'Coming Soon 2',
      path: '/pages/comingsoon2',
      component: () => import('@/views/pages/maintenance/comingsoon/ComingSoonPage2.vue')
    },
    {
      name: 'Under Construction 1',
      path: '/pages/construction1',
      component: () => import('@/views/pages/underconstruction/UnderConstruction1.vue')
    },
    {
      name: 'Under Construction 2',
      path: '/pages/construction2',
      component: () => import('@/views/pages/underconstruction/UnderConstruction2.vue')
    },
    {
      name: 'Error 404',
      path: '/pages/error',
      component: () => import('@/views/pages/maintenance/error/Error404Page.vue')
    },
    {
      name: 'Error 500', 
      path: '/pages/error500',
      component: () => import('@/views/pages/maintenance/error/Error500Page.vue')
    },
    {
      path: '/auth/callback',
      component: () => import('@/views/authentication/auth1/AuthCallback.vue'),
      meta: {
        requiresAuth: false,
        title: 'Authentication Callback'
      }
    },
    {
      path: '/auth',
      component: () => import('@/views/authentication/auth1/AuthCallback.vue'),
      meta: {
        requiresAuth: false,
        title: 'Authentication Callback'
      }
    }
  ]
};

export default AuthRoutes;
