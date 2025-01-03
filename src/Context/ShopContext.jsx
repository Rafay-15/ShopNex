import React, { createContext, useState, useEffect } from "react";
import all_product from "../Components/Assets/all_product";

export const ShopContext = createContext(null);

const ShopContextProvider = (props) => {
  const [cartItems, setCartItems] = useState([]);
  const [theme, setTheme] = useState("dark");

  // Load cart from localStorage on initial load
  useEffect(() => {
    const savedCartItems = JSON.parse(localStorage.getItem("cartItems"));
    if (savedCartItems) {
      setCartItems(savedCartItems);
    }
  }, []);

  // Persist cart to localStorage whenever it changes
  useEffect(() => {
    if (cartItems.length > 0) {
      localStorage.setItem("cartItems", JSON.stringify(cartItems));
    }
  }, [cartItems]);

  const addToCart = (itemId, size, quantity) => {
    const existingCartItemIndex = cartItems.findIndex(
      (item) => item.id === itemId && item.size === size
    );

    if (existingCartItemIndex !== -1) {
      const updatedCartItems = cartItems.map((item, index) => {
        if (index === existingCartItemIndex) {
          return {
            ...item,
            quantity: item.quantity + quantity,
          };
        }
        return item;
      });
      setCartItems(updatedCartItems);
    } else {
      const cartProduct = all_product.find((product) => product.id === itemId);
      cartProduct.size = size;
      cartProduct.quantity = quantity;
      setCartItems([...cartItems, cartProduct]);
    }
  };

  const removeFromCart = (itemId) => {
    const updatedCartItems = cartItems.filter((product) => product.id !== itemId);
    setCartItems(updatedCartItems);
  };

  const getTotalCartAmount = () => {
    return cartItems.reduce(
      (total, product) => total + product.new_price * product.quantity,
      0
    );
  };

  const getTotalCartItems = () => {
    return cartItems.length;
  };

  const contextValue = {
    all_product,
    cartItems,
    theme,
    addToCart,
    removeFromCart,
    getTotalCartAmount,
    getTotalCartItems,
    setTheme,
  };

  return (
    <ShopContext.Provider value={contextValue}>
      {props.children}
    </ShopContext.Provider>
  );
};

export default ShopContextProvider;
