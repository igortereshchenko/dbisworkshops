export const countUsersToOrders = ({usersKeys, ordersKeys}) => {
    const existingOrders = usersKeys.find(
        user => user === ordersKeys[0]
    );
    console.log(usersKeys, ordersKeys)
    return existingOrders;
};