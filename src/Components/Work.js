import React from "react";
import Feature1 from "../Assets/feature1.png";
import Feature2 from "../Assets/feature2.png";
import Feature3 from "../Assets/feature3.png";

const Work = () => {
  const workInfoData = [
    {
      image: Feature1,
      title: "Feature 1",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et ",
    },
    {
      image: Feature2,
      title: "Feature 2",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et ",
    },
    {
      image: Feature3,
      title: "Feature 3",
      text: "Lorem ipsum dolor sit amet consectetur. Maecenas orci et",
    },
  ];
  return (
    <div className="work-section-wrapper">
      <div className="work-section-top">
        {/* <p className="primary-subheading">Work</p> */}
        <h1 className="primary-heading">How It Works</h1>
        <p className="primary-text">
          Lorem ipsum dolor sit amet consectetur. Non tincidunt magna non et
          elit. Dolor turpis
        </p>
      </div>
      <div className="work-section-bottom">
        {workInfoData.map((data) => (
          <div className="work-section-info" key={data.title}>
            <div className="info-boxes-img-container">
              <img src={data.image} alt="" />
            </div>
            <h2>{data.title}</h2>
            <p>{data.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Work;
