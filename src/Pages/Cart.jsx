import React from 'react'
import CartItems from '../Components/CartItems/CartItems'
import { Helmet } from 'react-helmet-async';

const Cart = () => {
  return (
    <div>
      <Helmet>
        <title>Cart</title>
      </Helmet>
      <CartItems/>
    </div>
  )
}

export default Cart
