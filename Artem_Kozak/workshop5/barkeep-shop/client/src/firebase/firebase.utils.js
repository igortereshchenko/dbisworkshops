import firebase from 'firebase/app';
import 'firebase/analytics';
import 'firebase/firestore';
import 'firebase/auth';

const config = {
    apiKey: "AIzaSyDZV38RO1Led2MAt7cl7Yi0yJQIT1pxAmA",
    authDomain: "barkeep-shop.firebaseapp.com",
    databaseURL: "https://barkeep-shop.firebaseio.com",
    projectId: "barkeep-shop",
    storageBucket: "barkeep-shop.appspot.com",
    messagingSenderId: "351259110076",
    appId: "1:351259110076:web:0102838b70d4bac549feb9",
    measurementId: "G-X5MLSJ6SJS"
};

firebase.initializeApp(config);
firebase.analytics();

export const createUserProfileDocument = async (userAuth, additionalData) => {
    if (!userAuth) return;

    const userRef = firestore.doc(`users/${userAuth.uid}`);

    const snapShot = await userRef.get();

    if (!snapShot.exists) {
        const {uid, displayName, photoURL = '', email, emailVerified = false, phoneNumber = null, isAnonymous = false} = userAuth;
        const createdAt = new Date();
        const address = null;
        const loyaltyPoints = 0;
        try {
            await userRef.set({
                uid,
                displayName,
                photoURL,
                email,
                emailVerified,
                phoneNumber,
                isAnonymous,
                createdAt,
                address,
                loyaltyPoints,
                ...additionalData
            });
        } catch (error) {
            console.log('error creating user', error.message);
        }
    }

    return userRef;
};

export const createUserOrderDocument = async (orderData) => {
    if (!orderData) return;

    const orderRef = firestore.collection(`users/${orderData.orderUserData.uid}/orders`);

    const currentUser = orderData.orderUserData;
    const cartItems = orderData.cartItems;
    const total = orderData.total;
    const createdAt = new Date();
    const orderStatus = 0 // 0 - New order, 1 - Processed, 2 - Delivering, 3 - Received by customer
    try {
        await orderRef.doc().set({
            currentUser,
            cartItems,
            total,
            createdAt,
            orderStatus
        });
    } catch (error) {
        console.log('error creating order', error.message);
    }
};

export const updateUserProfileDocument = async ({userAuth, displayName, email, phoneNumber, address}) => {
    const userRef = firestore.doc(`users/${userAuth.uid}`);
    await userRef.update({
        displayName,
        email,
        phoneNumber,
        address
    });
}

export const updateAdminUserStatusDocument = async ({userId, orderId, orderStatus}) => {
    const userRef = firestore.doc(`users/${userId}/orders/${orderId}`);
    await userRef.update({
        orderStatus
    });
}

// export const addCollectionAndDocuments = async (collectionKey, objectsToAdd) => {
//     const collectionRef = firestore.collection(collectionKey);
//
//     const batch = firestore.batch();
//     objectsToAdd.forEach(obj => {
//         const newDocRef = collectionRef.doc();
//         batch.set(newDocRef, obj);
//     });
//
//     return await batch.commit();
// };

export const convertCollectionsSnapshotToMap = collections => {
    const transformedCollection = collections.docs.map(doc => {
        const {title, route, items} = doc.data();

        return {
            routeName: encodeURI(route.toLowerCase()),
            id: doc.id,
            route,
            title,
            items
        };
    });

    return transformedCollection.reduce((accumulator, collection) => {
        accumulator[collection.route.toLowerCase()] = collection;
        return accumulator;
    }, {});
};

export const convertUserOrdersSnapshotToMap = userOrders => {
    const transformedUserOrders = userOrders.docs.map(doc => {
        const {cartItems, createdAt, currentUser, orderStatus, total} = doc.data();

        return {
            routeName: encodeURI(doc.id),
            id: doc.id,
            cartItems,
            createdAt,
            currentUser,
            orderStatus,
            total,
        };
    });
    return transformedUserOrders.reduce((accumulator, userOrder) => {
        accumulator[userOrder.id] = userOrder;
        return accumulator;
    }, {});
};

export const convertUsersSnapshotToMap = users => {
    const transformedUsers = users.docs.map(doc => {
        const {
            uid,
            displayName,
            photoURL,
            email,
            emailVerified,
            phoneNumber,
            isAnonymous,
            createdAt,
            address,
            loyaltyPoints,
        } = doc.data();

        return {
            uid,
            displayName,
            photoURL,
            email,
            emailVerified,
            phoneNumber,
            isAnonymous,
            createdAt,
            address,
            loyaltyPoints,
        };
    });

    return transformedUsers.reduce((accumulator, users) => {
        accumulator[users.uid] = users;
        return accumulator;
    }, {});
};


export const convertAdminUsersOrdersSnapshotToMap = orders => {
    const transformedOrders = orders.docs.map(doc => {
        const {
            cartItems,
            currentUser,
            orderStatus,
            total,
            createdAt,
        } = doc.data();
        const id = doc.id;

        return {
            cartItems,
            currentUser,
            orderStatus,
            total,
            createdAt,
            id
        };
    });

    return transformedOrders.reduce((accumulator, orders) => {
        accumulator[orders.id] = orders;
        return accumulator;
    }, {});
};

export const getCurrentUser = () => {
    return new Promise((resolve, reject) => {
        const unsubscribe = auth.onAuthStateChanged(userAuth => {
            unsubscribe();
            resolve(userAuth);
        }, reject);
    });
};

// export const getOrdersCollections = () => {
//     const orders = firebase.firestore().collectionGroup('orders')
//     orders.get().then(function (querySnapshot) {
//         querySnapshot.forEach(function (doc) {
//             console.log(doc.id, ' => ', doc.data());
//         });
//     });
// }


// (currentUser.id === 'JOZY7zzZx9fsgna5BBGWuIIJHzi2')

export const auth = firebase.auth();
export const firestore = firebase.firestore();

export const googleProvider = new firebase.auth.GoogleAuthProvider();
googleProvider.setCustomParameters({prompt: 'select_account'});

export const facebookProvider = new firebase.auth.FacebookAuthProvider();
facebookProvider.setCustomParameters({prompt: 'select_account'});

export default firebase;
