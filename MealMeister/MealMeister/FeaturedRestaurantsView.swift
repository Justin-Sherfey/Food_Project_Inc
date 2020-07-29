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
            List(viewModel.restaurants) { Restaurant in
                VStack(alignment: .leading) {
                    Text(Restaurant.displayName)
                        .font(.headline)
                    Text(Restaurant.name)
                        .font(.subheadline)
                    Text(Restaurant.tag)
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
