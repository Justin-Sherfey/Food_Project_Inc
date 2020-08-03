//
//  FeaturedRestaurantsView.swift
//  MealMeister
//
//  Created by Brett Beattie on 7/29/20.
//  Copyright © 2020 Andrew Thomas. All rights reserved.
//

import SwiftUI

struct FeaturedRestaurantsView: View {
    @ObservedObject private var viewModel = RestaurantViewModel()
    
    var body: some View {
        NavigationView {
            List(viewModel.restaurants) { restaurant in
                VStack(alignment: .leading) {
                    Text(restaurant.name)
                        .font(.headline)
                    Text("\(restaurant.rating) stars")
                        .font(.subheadline)
                }
            }
            .navigationBarTitle("Featured Restaurants")
            .onAppear() {
                self.viewModel.fetchData()
            }
        }
    }
}

struct FeaturedRestaurantsView_Previews: PreviewProvider {
    static var previews: some View {
        FeaturedRestaurantsView()
    }
}

