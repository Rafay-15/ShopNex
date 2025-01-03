import React, { useContext } from "react";
import { ShopContext } from "../Context/ShopContext";
import { useParams } from "react-router-dom";
import Breadcrum from "../Components/Breadcrums/Breadcrum";
import ProductDisplay from "../Components/ProductDisplay/ProductDisplay";
import DescriptionBox from "../Components/DescriptionBox/DescriptionBox";
import RelatedProducts from "../Components/RelatedProducts/RelatedProducts";
import ReviewSection from "../Components/ReviewSection/ReviewSection";
import { Helmet } from 'react-helmet-async';

const Product = () => {
  const { all_product } = useContext(ShopContext);
  const { productId } = useParams();
  const product = all_product.find((e) => e.id === Number(productId));
  return (
    <div>
      <Helmet>
        <title>Product</title>
      </Helmet>
      <Breadcrum product={product} />
      <ProductDisplay product={product} />
      <DescriptionBox />
      <ReviewSection />
      <RelatedProducts />
    </div>
  );
};

export default Product;
