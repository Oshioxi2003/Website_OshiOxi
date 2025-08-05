import { usePricingPlans } from '../../../hooks';
import PricingCard from '../../common/PricingCard';

const PricingAreaHomeOne = () => {
  const { data: pricingPlans, loading, error } = usePricingPlans();

  if (loading) {
    return (
      <div className="section-space-top section-space-md-bottom">
        <div className="container">
          <div className="text-center">
            <div className="spinner-border text-primary" role="status">
              <span className="visually-hidden">Loading...</span>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="section-space-top section-space-md-bottom">
        <div className="container">
          <div className="text-center text-danger">
            <p>Error loading pricing plans: {error.message}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <>
       <div className="section-space-top section-space-md-bottom">
      <div className="section-space-sm-bottom">
        <div className="container">
          <div className="row justify-content-center">
            <div className="col-lg-10 col-xl-8">
              <div className="d-flex justify-content-center align-items-center flex-wrap row-gap-2 column-gap-4"
                data-cue="fadeIn">
                <div className="flex-shrink-0 d-inline-block w-10 h-2px bg-primary-gradient"></div><span
                  className="d-block fw-medium text-light fs-20">Pricing Plan</span>
              </div>
              <h2 className="text-light text-center mb-0" data-cue="fadeIn">Choose Your Most Suitable Pricing Plan</h2>
            </div>
          </div>
        </div>
      </div>
      <div className="section-space-xsm-bottom">
        <div className="container">
          <div className="row" data-cue="fadeIn">
            <div className="col-12">
              <div className="d-flex justify-content-center align-items-center row-gap-2 column-gap-4"><button type="button"
                  className="btn btn-primary-gradient text-white fs-14 border-0 rounded-pill"><span
                    className="d-inline-block">Billed Monthly </span><span className="d-inline-block"><i
                      className="bi bi-arrow-right"></i></span></button> <button type="button"
                  className="btn btn-outline-danger fs-14 rounded-pill"><span className="d-inline-block">Billed Yearly
                  </span><span className="d-inline-block"><i className="bi bi-arrow-right"></i></span></button></div>
            </div>
          </div>
        </div>
      </div>
      <div className="container">
        <div className="row g-4 align-items-center" data-cues="fadeIn">
          {pricingPlans && pricingPlans.length > 0 ? (
            pricingPlans.map((plan) => (
              <PricingCard key={plan.id} plan={plan} />
            ))
          ) : (
            <div className="col-12 text-center">
              <p className="text-light text-opacity-75">No pricing plans available.</p>
            </div>
          )}
        </div>
      </div>
    </div>
    </>
  );
};

export default PricingAreaHomeOne;