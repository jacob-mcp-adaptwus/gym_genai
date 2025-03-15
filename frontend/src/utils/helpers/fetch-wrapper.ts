import { useAuthStore } from '@/stores/auth';

export const fetchWrapper = {
  get: request('GET'),
  post: request('POST'),
  put: request('PUT'),
  delete: request('DELETE')
};

interface temp {
  method: string;
  headers: Record<string, string>;
  body?: string;
}

interface UserData {
  username: string;
  password: string;
}

function request(method: string) {
  return (url: string, body?: object) => {
    const requestOptions: temp = {
      method,
      headers: authHeader(url)
    };
    if (body) {
      requestOptions.headers['Content-Type'] = 'application/json';
      requestOptions.body = JSON.stringify(body);
    }
    return fetch(url, requestOptions).then(handleResponse);
  };
}

// helper functions
function authHeader(url: string): Record<string, string> {
  // return auth header with jwt if user is logged in and request is to the api url
  const { cognitoUser } = useAuthStore();

//   this is cognito object {
//     "id_token": "eyJraWQiOiJES0RTVXkweHpBekZOQ3BwK2ZGdzBlNlwvNGwrbVNGcEtsUEdlSUV6MzFUYz0iLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiTkppd2tzcngyTzltenpNN0l6djd5dyIsInN1YiI6IjgxMmI2NWMwLWQwZDEtNzA0NS1hZTUwLTU2NzZlM2FjYjUwNSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9ERlBlYzJMVWgiLCJjb2duaXRvOnVzZXJuYW1lIjoiODEyYjY1YzAtZDBkMS03MDQ1LWFlNTAtNTY3NmUzYWNiNTA1IiwiZ2l2ZW5fbmFtZSI6IkphY29iIiwib3JpZ2luX2p0aSI6IjQwZjRiYjRlLTBkMjItNGMyZS04MWViLTkyZWNlODAyOGYxZCIsImF1ZCI6IjY1c2lmZGg5bG5tZHRtZHZjbjM3dmFyMWlpIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE3MzUzMzQxMTksImV4cCI6MTczNTMzNzcxOSwiaWF0IjoxNzM1MzM0MTE5LCJmYW1pbHlfbmFtZSI6Ik1jUGhpbGxpcHMiLCJqdGkiOiI1MmI4NWViYi1jOGU0LTQ4NWItODAyOC1iYzlmOWE3OGU5YTciLCJlbWFpbCI6ImphY29iLm1jcGhpbGxpcHNAZ21haWwuY29tIn0.kyzuUF7ny2VzSejOQhuQn75kSQMXX6J5mFBe9QUGK1NYAdsgwbwkChfbXDgQA1gbdVM4pobhimb3joSMlrJ56WuAtbB80v4Q8S2tQ2RxEHTBP9QsmD6B2J1Mu7aDkNeBcepjj6Cp73SS-75ITFDtZgizS-yBQbtASPN1fsP06vxnMOMEtFoNbdvyMyFnT6eUsNDiPvZl1DX4bc9FPqWpuo2XPVW1BcARODNJ3SNAsDd9gWVTuQ8IDhX-Q3kKbHTp00wrkxUVREVZS6XnBXV3WYH8SSPB2ZflKNv-r5_Ti-t_8-gOkYk6R1mF30j5udNSox-tSp3J6bIKiocEoiv8YA",
//     "session_state": null,
//     "access_token": "eyJraWQiOiJPMnA2bHBYRU9SRVwvMlVQNElYYWw1aU1Qd1V1Sm5XbENzQlFjb1Z2M2swUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4MTJiNjVjMC1kMGQxLTcwNDUtYWU1MC01Njc2ZTNhY2I1MDUiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9ERlBlYzJMVWgiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI2NXNpZmRoOWxubWR0bWR2Y24zN3ZhcjFpaSIsIm9yaWdpbl9qdGkiOiI0MGY0YmI0ZS0wZDIyLTRjMmUtODFlYi05MmVjZTgwMjhmMWQiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6Im9wZW5pZCIsImF1dGhfdGltZSI6MTczNTMzNDExOSwiZXhwIjoxNzM1MzM3NzE5LCJpYXQiOjE3MzUzMzQxMTksImp0aSI6ImNlMWMwNjVlLTdmODEtNDc3Yi1iMTgwLWNkMDNiNTE3YjgyYSIsInVzZXJuYW1lIjoiODEyYjY1YzAtZDBkMS03MDQ1LWFlNTAtNTY3NmUzYWNiNTA1In0.qEU9YUhzcIVee9XMOVLefMa2mJodFL3tL535P1fAie1JkB0ysLS4oysrWpDXkQJi_V4Z1yXvh7wj23zxVpieq5rXpsLSnHh_MM_8iqMwVfEzE_T5eJ_2PuaGB5VZd6LkkYVcGsVH2rC6QAcpO2gtNbiNXf6XAMOLK5UUbRl7aJl9kxNVl55zn0VRcMMy3fAGHw4gi1PUekRF0eQfGY0LOUikC2Kp-wKN8bHX_94onafV_qTd2GvUpgatBZkCyxIU7BiUJ2FDwZUCSWdi-X79WJTn6qqLNeTXap62BVoAD8BzhZ2lB0djux3ImMlsuNQPINM5GgrHWmxLGxIZ9wqvyQ",
//     "refresh_token": "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ltWTPyCE8obK4Bt54-tWJsLj8nXFYSfA5OgyxHUlW42Kn81QlLCRqXblTb_UtNPUcDZFaTaao-XocV8YbSXRyJOqzJ4dT6NFUzJ9ICJv0qFWnIptkPx3Dk8JD3ew-Ibp9vgHTH2bYtL-AkeCZx6z24LZmAVCnOB8JaFg7eyCVicsKoJ81hvvx8tK5RDYkiBuX67nNz6LovZdfHehJDejqWygu9fX9LgtN-dy9Lrlxv4pvL--PwVBFQFvWMXmqpKKn1IYb_4pSfRC11ch3U3yVwnfHKd58SzxuhvpMFcbPeO_F2_7zwRe_EFgHA2-NVXzwilmDDa-ZG-ouMDBA9tgng.kUFBbu8C4_hfDocj.AGX6E3cAz4JjeHgEPAaMRu3BEbZ1b8bLA7GDRD9XTA6t-iZqPa7LEqMN1R2AUDXwaLbDBrUQ_MJZwVEEvksBsTntg-A1mQoQQbItHg3TGDrzQOJch10Q_1sy78u8rgHXG_ltqDhm3Aywv0JsbL58-3iv_BE7Y9xvKeYpVMZydunwuDCT9_xqvjnDOi1yA6GE4zktWuQqqXFekqG0KrQuGAeMD4eTQOa8E2PckHIlUUfTCEBQXSw-0qZCAeOo2HFK5JG3piBA9Dv9xAN3nsOYnl9S05qbAS610cYI64TSOC-LaASuylw6Tmk_kqAhN6gcMEeRei0nWPQkjlGGdBG0tnCY8jYIo8UA1dne2cyib_Md-ya6pjEJrkGIiNzWKs9o3k93wsG_RytRvwxQ3LCD6-Wl9hQvgJdjgupsF290XIcBEhXsywMSA0X8JBjGKBFSpFEdZHVWOFNTnAddqqZeO0egsJTRrCPCrsVXW__6EbiQSYEeIjJvvrI1GN9fGNKP9lBgZtM0mqIPC5NPeXwImytCfjQ9ObPOb-Uvrcb8TcnVM7hPXA_Ge2nzDQirNrEM4bwpkROrQ8GfGhWjWUGY56AtF5jRyR74x-kDk7-oHwOivhZq7XoLYBU0HiW_Du9ecM9TWDn0JN2qyiJFkGxA_WnqiBf7Q4felfkYRwiY_IZOI6wvbT1AQJO4GEeViyRexLG7kMnrVEs0JrXcVj7JSZTAQMiCfrLprMUMBtXcHWY8YB20fxNpLLA3__jFRuR3aotoWQ7ssufvA3yCiRVt_Ko-dD2Z5RL_4BxTCnRKAHd71QlJQEQaIs2lABS_tuxm8JyhgrbEw2lBzpCQZgqzfEjJTyIm5bMKkhreMQL7-HvsSI8xHh6HpLV5JtKPQ727mecHKmrFxddSoJMmgq1Wh66gJozAXMz_0EtY3Bkoj6W8Mng3qN3iLxL-dxxL2-0bacCqOpVwQYmp355JH58UwW-rG2B2yshn_R8PUdHXT2jsb73FYa6IMjfhtzqNrJLeVqI-7i3c8crts9hEmTZiPbKgIGrWB14dFq1ElUa4s5QbsywY6-bFiQdzDKS_YdFEBVXvlAzMIMKO2JIKH2XtA2bf8w_40gHHPH_UX_1J3NBYAdz_4md3gxp1zmRCL092DT_9CbTPW8j5Y8tAMiiCNim0CfYIrjlTyLPmRXMVlTsG3vpjIrGA0vE_phuI_uuuzQWavoKEF5JfKg.Ayw20qQvJ8ec5WRivBpKbQ",
//     "token_type": "Bearer",
//     "scope": "openid",
//     "profile": {
//         "sub": "812b65c0-d0d1-7045-ae50-5676e3acb505",
//         "email_verified": "true",
//         "iss": "https://cognito-idp.us-east-2.amazonaws.com/us-east-2_DFPec2LUh",
//         "cognito:username": "812b65c0-d0d1-7045-ae50-5676e3acb505",
//         "given_name": "Jacob",
//         "origin_jti": "40f4bb4e-0d22-4c2e-81eb-92ece8028f1d",
//         "aud": "65sifdh9lnmdtmdvcn37var1ii",
//         "token_use": "id",
//         "exp": 1735337719,
//         "iat": 1735334119,
//         "family_name": "McPhillips",
//         "email": "jacob.mcphillips@gmail.com",
//         "username": "812b65c0-d0d1-7045-ae50-5676e3acb505"
//     },
//     "expires_at": 1735337719
// }
  if (cognitoUser && cognitoUser.id_token) {
    return { Authorization: `Bearer ${cognitoUser.id_token}` };
  } else {
    console.log("no bearer token");
    return {};
  }
}


function handleResponse(response: Response): Promise<UserData> {
  return response.text().then((text: string) => {
    const data = text && JSON.parse(text);

    if (!response.ok) {
      const { cognitoUser, logout } = useAuthStore();
      if ([401, 403].includes(response.status) && cognitoUser) {
        // auto logout if 401 Unauthorized or 403 Forbidden response returned from api
        logout();
      }

      const error: string = (data && data.message) || response.statusText;
      return Promise.reject(error);
    }

    // Ensure data is of type UserData
    return data as UserData;
  });
}
